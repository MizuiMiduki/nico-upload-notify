# coding: utf-8

import feedparser
import os
from misskey import Misskey

f = open("date.txt", "r")
old_up = f.readline().replace("\n", "")
f.close()

entries = feedparser.parse('https://www.nicovideo.jp/user/'+str(os.environ.get("NICONICO_USER_ID"))+'/video?rss=2.0&lang=ja')['entries']
print('https://www.nicovideo.jp/user/'+str(os.environ.get("NICONICO_USER_ID"))+'/video?rss=2.0&lang=ja')

i = 0
max_entry = len(entries)

while (True):
    print(i)
    print(max_entry)
    now_entry = entries[i]
    if now_entry['updated'] == old_up or i+1 == max_entry:
        new_up = entries[0]['updated']
        g = open("date.txt", "w")
        g.write(new_up)
        g.close()
        break
    else:
        title = now_entry['title']
        page_url_base = now_entry['link']
        page_url = page_url_base.replace('?ref=rss_myvideo_rss2.0','')
        id_hashtag = '#'+page_url.replace('https://www.nicovideo.jp/watch/','')
        post_text ="動画を投稿しました\n"+title + "\n" + page_url+"\n\n#ニコニコ動画\n"+id_hashtag
        print(post_text+"\n")
        #SNS投稿API
        # Misskey
        api = Misskey(os.environ.get("MISSKEY_SERVER_ADDRESS"))
        api.token = os.environ.get("MISSKEY_TOKEN")
        api.notes_create(text=post_text)
    i += 1
