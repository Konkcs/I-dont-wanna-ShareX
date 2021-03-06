"""
Custom server for uploading ShareX images and displaying them with a nice embed in discord.
Clean looking website with a way to delete images if you are the uploaded (using api keys)

Must edit lines: 12, 13, 17, 71
"""
from flask import Flask, render_template, request
import hurry.filesize, secrets, json, os
from os.path import splitext
from PIL import Image

author_name = 'NAME FOR ABOVE IMAGES'
api_key = 'API_KEY' # <-- set your api key/secret key here

app = Flask(__name__)
storage_folder = 'static/screenshots/images'
website_url = 'http://www.example.com' # If hosting from home redirect www.url.com --> home IP and use http instead of https

@app.route('/')
def index():
    return render_template('index.html', URL=website_url)

@app.route('/<page>')
def screenshoturl(page):
    if f'{page}.png' not in os.listdir(storage_folder):
        return render_template('404.html', URL=website_url)

    uploader = 'N/A'
    try:
        with open(f'static/screenshots/json/{page}.json') as f:
            uploader = json.load(f)["author_name"]
    except Exception as e:
        print(e)
        pass
    return render_template('sstemplate.html',
                           ss_location=f'{website_url}/static/screenshots/images/{page}.png',
                           json_location=f'{website_url}/static/screenshots/json/{page}.json',
                           upload_username=uploader,
                           cur_url=page)

@app.route('/upload', methods=['POST']) # https://github.com/kvcvc/flask-sharex <-- Modified upload script
def upload():
    if not request.method == 'POST':
        return {"error": "Method Not Allowed"}, 405
    used_api_key = request.form.to_dict(flat=False)['secret_key'][0]

    if used_api_key == api_key:
        file = request.files['image']
        extension = splitext(file.filename)[1]
        file.flush()
        size = os.fstat(file.fileno()).st_size
        '''Check for file extension and file size.'''
        if extension != '.png':
            return 'File type is not supported', 415

        elif size > 6000000:
            return 'File size too large', 400

        else:
            '''Remove metadata of the file.'''
            image = Image.open(file)
            data = list(image.getdata())
            file_without_exif = Image.new(image.mode, image.size)
            file_without_exif.putdata(data)
            '''Save the image with a new randomly generated filename in the desired path, and return URL info.'''
            filename = secrets.token_urlsafe(8)
            file_without_exif.save(os.path.join(storage_folder, filename + extension))

            image_json = {"title": filename + '.png',
                          "author_name": author_name,
                          "author_url": website_url, # "https://www.example.com" <--- Where ever you want your embed title to link to
                          "provider_name": hurry.filesize.size(size, system=hurry.filesize.alternative)}

            with open(f'static/screenshots/json/{filename}.json', 'w+') as f:
                json.dump(image_json, f, indent=4)
            return json.dumps({"filename": filename, "extension": extension}), 200
    else:
        return 'Unauthorized use', 401

@app.route('/delete')
def delete():
    del_url = request.args.get('del_url')
    used_api_key = request.args.get('api_key')
    if f"{del_url}.png" in os.listdir('static/screenshots/images'):

        if used_api_key == api_key:
            os.remove(f'static/screenshots/images/{del_url}.png')
            os.remove(f'static/screenshots/json/{del_url}.json')
            return render_template('deleted.html', URL=website_url), 200
        else:
            return render_template('bad_key.html', URL=website_url), 401
    else:
        return render_template('404.html', URL=website_url), 404

app.run("0.0.0.0", 80)
