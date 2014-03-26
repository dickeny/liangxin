#!/usr/bin/python
#-*- coding: UTF-8 -*-

import model
from pprint import pprint
from urllib2 import urlopen
from BeautifulSoup import BeautifulStoneSoup as BSS

def load():
    url = "http://www.sdlufu.com/"
    do_load(url)
    for i in range(1, 20):
        url = "http://www.sdlufu.com/list/%d/" % i
        do_load(url)

def do_load(surl):
    txt = urlopen(surl).read().decode("GBK")
    soup = BSS(txt)
    qvods = {}
    titles = {}
    for a in soup.findAll("a"):
        url = a['href']
        if 'qvod' in url:
            _, idx, qvod_url = url.replace("&url", "").split("=")
            qvods[idx] = qvod_url
        elif a.has_key('title') and '/av/' in url:
            idx = url.replace("/av/", "").replace(".html", "")
            titles[idx] = a['title'].replace("|", "")
    pprint(qvods)
    pprint(titles)
    for idx, url in qvods.items():
        title = titles[idx]
        try:
            model.new_movie(idx, title, title, url, u"ady映画");
        except:
            pass

if __name__ == "__main__":
    load()

