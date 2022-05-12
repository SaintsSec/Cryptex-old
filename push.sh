#!/bin/bash
# push to git hub
# created by : cosmo

git fetch
git pull origin master
git add .
git commit -m "$1"
git push -u origin master
