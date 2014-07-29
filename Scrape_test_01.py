# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 19:17:53 2014

@author: Kazunari
"""

import urllib2
import cookielib

base_url = 'http://chotatsu.mlit.go.jp/new_kensaku/BuppinZuiList.asp?str='
ua = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'

#本当はCookieを動的に獲得したいんですけどこれだと上手く動かなかったんです
#r = urllib2.urlopen('http://chotatsu.mlit.go.jp/Reference.asp')
#headers = r.info()
#ck = headers.getheader("Set-Cookie")

ck = 'ASPSESSIONIDSCRSBQSB=LNFMHOGDPMEHCAAAANBNCIEH'

for i in range(10):
    url = base_url + str(i+1)
    req = urllib2.Request(url,headers={'User-Agent' : ua,'Cookie' : ck})
    html = urllib2.urlopen(req).read()
    f = open("mlit_tender_html",'a')
    f.write(html)
    print url
f.close()

#これ以降は文字列処理
mlit_tender = open("mlit_tender_html",'w')

#置換用ヘッダ、フッタの呼び出し
header_noise = open("noise_header.txt",'r')
footer_noise = open("noise_footer.txt",'r')

mlit_tender = mlit_tender.replace(header_noise,"")
mlit_tender = mlit_tender.replace(footer_noise,"")
mlit_tender = mlit_tender.replace('\r\n',"")

d = open("mlit_tender.tsv",'w')
d.write(mlit_tender)
d.close()