#!/bin/bash

# pull it into your dropbox
scp urls.txt user@server:~/podify/
ssh user@server 'cd ~/podify/ && ./podify.py'
scp user@server:~/podify/pods/* ~/Dropbox/pods/
ssh user@server 'rm ~/podify/pods/*'
