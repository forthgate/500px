# 500px
Script for 500px account promotion (auto-like)

  This is my first script on Python 3, so if you have some questions or suggestions  or you find mistakes in my code, contact me forthgate@gmail.com 


  This script helps to promote account and allow like over 16200 photos per day on 500px.com. When script will be launched it will open page with fresh photos and start like every picture. When 20 pics will be liked, page will refresh and script start from beginning. For statistic i put counter for every liked pic. Script contains infinite loop, so keep in mind it

## Dependencies:
On your OS should be installed Chromium/Chrome ==>71.0.0 and python3-pip package<br>

## How to start:
At first you should to add two variables - $USER and $PASSWORD which will be used for authorization:
```
export USER='USER'
export PASSWORD='YOUR_PASSWORD'
```
Then you should to install requrement modules
`pip install -r requrirements.txt`

After this you can launch the script:

`python3 500px.com` or `python3 500px.com &` to start in background

Or you can run  script **start.sh** (set variables inside start.sh before launch. This script contain inifite loop)

## Docker:
To build docker image:
```
docker build -t 500px-promote .
```
Set variables in .env file and start container:
```
docker run --env-file .env -d 500px-promote
```
____________________________________________________________________________________________________________________________
This script was tested on Debian/CentOS/Arch. 
