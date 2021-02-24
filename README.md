# ShareX-discord-embed-uploader
Flask website to upload sharex images and display them in discord with an embed

# Installation

* Install python
```
pip install hurry.filesize
pip install dnspython
pip install pillow
pip install flask
```

# Setup
* If you're running from home you need to forward port 80
* In main.py you need to:
  * line 12: Set your author name for above screenshots (On the website/discord embed) 
  * line 13: Set your API key (Used for uploading and deleting images)
  * line 17: Set your website URL
  * line 71: Set your embed title url (where it should take someone when they click it)
* Run "main.py"
* Open "ShareX.sxcu" in a text editor and change:
  * line 6: Change "https://www.example.com" to your url
  * line 9: Change "API_KEY" to the same api key you set in main.py
  * line 12: Change "http://www.example.com" to your url
* Run "ShareX.sxcu" (double click it)



# If you need any help you can either join [Discord](https://discord.gg/uf8KCFhPch) or add me Konk#1337
