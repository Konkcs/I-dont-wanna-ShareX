# ShareX-discord-embed-uploader
Flask website to upload sharex images and display them in discord with an embed

# Installation

* Install python
* pip install all requirements in requirements.txt

# Setup
* for MongoDB you need to:
  * Create a [MongoDB account](https://www.youtube.com/watch?v=rE_bJl2GAY8)
  * Create a cluster called "sharex"
  * Create a colllection called "api keys"
  * If you're NOT using the discord bot (link soon) you will need to add an entry to the collection with the fields: {"\_id": "0", "api_key": "A SECRET KEY HERE"}
* In main.py you need to
  * line 14: set your MongoDB connection link (video above explains where/how to get it
  * line 21: set your website URL
  * line 76: set your embed title url (where it should take someone when they click it)
* run main.py and enjoy :)

[Discord](https://discord.gg/uf8KCFhPch) Konk#1337
