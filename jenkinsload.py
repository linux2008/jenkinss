#!/usr/bin/python

import urllib,urllib2
import os

URL_LASTVER="http://192.168.235.130/deploy/lastver"
URL_LIVEVER="http://192.168.235.130/deploy/livever"
URL_PKG="http://192.168.235.130/deploy/packages/"
DOWNLOAD_DIR="/var/www/download/"
DEPLOY_DIR="/var/www/deploy/"
APP_NAME="wordpress"

def init():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    if not os.path.exists(DEPLOY_DIR):
        os.makedirs(DEPLOY_DIR)


def getURL(url):
    return urllib2.urlopen(url).read().strip()

def checkLastVersion():
    lastver=getURL(URL_LASTVER)
    url_pkg_path=URL_PKG +"%s-%s.tar.gz" %(APP_NAME,lastver)
    pkg_path=os.path.join(DOWNLOAD_DIR,"%s-%s.tar.gz" %(APP_NAME,lastver))
    data=getURL(url_pkg_path)
    if not os.path.exists(pkg_path):
        with open(pkg_path,'wb') as fd:
            fd.write(data)


if __name__=="__main__":
    init()
    checkLastVersion()
