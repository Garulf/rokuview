# rokuview
Capture screen and download off Roku based devices

# Requirements

This script requires that you have Devoloper mode activated on your Roku device.
Instructions on how to activate Devoloper mode can be found here: 
https://developer.roku.com/docs/developer-program/getting-started/developer-setup.md

# Usage: 
```
roku_snapshot.py [-h] [-p FILE_PATH] [--file-name FILE_NAME] username password host

  positional arguments:
  username (rokudev)
  password
  host (IP address or hostname with 'http' or 'https'

optional arguments:
  -h, --help            show this help message and exit
  -p FILE_PATH, --file-path FILE_PATH
  --file-name FILE_NAME
```

Example: python3 rokuview.py 'rokudev' '<PASSWORD>' '10.0.0.10' --file-path '/Volumes/Pictures' --file-name 'my_tv.jpg'
