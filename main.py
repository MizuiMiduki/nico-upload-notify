# coding: utf-8

import feedparser
import os
from misskey import Misskey

f = open("date.txt", "r")
old_up = f.readline().replace("\n", "")
f.close()

entries = feedparser.parse('https://www.nicovideo.jp/user/'+str(os.environ.get("NICONICO_USER_ID"))+'/video?rss=2.0&lang=ja')['entries']
print('https://www.nicovideo.jp/user/'+str(os.environ.get("NICONICO_USER_ID"))+'/video?rss=2.0&lang=ja')
