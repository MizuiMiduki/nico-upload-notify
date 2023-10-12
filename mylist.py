# coding: utf-8

import feedparser
import os
from misskey import Misskey
from atproto import Client , models

f = open("mylist-date.txt", "r")
old_up = f.readline().replace("\n", "")
f.close()

entries = feedparser.parse('https://www.nicovideo.jp/user/'+str(os.environ.get("NICONICO_USER_ID"))+'/mylist?rss=2.0&lang=ja-jp')['entries']

i = 0
max_entry = len(entries)

while (True):
    print(i+1)
    print(max_entry)
    now_entry = entries[i]
    if now_entry['updated'] == old_up or i+1 == max_entry:
        new_up = entries[0]['updated']
        g = open("mylist-date.txt", "w")
        g.write(new_up)
        g.close()
        break
    else:
        page_title = now_entry['title']
        page_url_base = now_entry['link']
        page_url = page_url_base.replace('?ref=rss_user_mylist_rss2.0','')
        id_hashtag = '#'+page_url.replace('https://www.nicovideo.jp/watch/','')
        post_text ="【マイリストに追加しました】\n"+page_title + "\n" + page_url+"\n\n#ニコニコ動画\n"+id_hashtag
        print(post_text+"\n")
        #SNS投稿API
        #Misskey
        misskey = Misskey(os.environ.get("MISSKEY_SERVER_ADDRESS"))
        misskey.token = os.environ.get("MISSKEY_TOKEN")
        misskey.notes_create(text=post_text)
        #bluesky
        bluesky = Client()
        bluesky.login(str(os.environ.get("BLUESKY_MAIL_ADDRESS")),str(os.environ.get("BLUESKY_PASSWORD")))
        embed_external = models.AppBskyEmbedExternal.Main(
            external = models.AppBskyEmbedExternal.External(
                title = page_title,
                description = "ニコニコ動画",
                uri = page_url
            )
        )
        bluesky.send_post("【マイリストに追加しました】\n"+page_title + "\n" + "\n\n#ニコニコ動画\n"+id_hashtag,embed = embed_external)

    i += 1
