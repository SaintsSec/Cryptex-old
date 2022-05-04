#!/bin/bash
# push to git hub
# created by : cosmo

git pull origin master
git add .
git commit -s -m "$1"
git push -u origin master
