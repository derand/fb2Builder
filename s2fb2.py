#!/usr/bin/env python
# -*- coding: utf-8 -*-
# developed by Andrew Derevyagin (2derand@gmail.com) special for http://www.suzumiya.ru
# 

import sys
import os
import re, binascii
import urllib
from PIL import Image
import time


presets = {
	'vol1': {
			'header': {
				'author-first-name':				'Нагару',
				'author-last-name':					'Танигава',
				'book-title':						'Меланхолия Харухи Судзумии',
				'coverpage-image_link':				'http://www.suzumiya.ru/local--files/v01t01-images/v01t01_cover_cut.jpg',
				'translator-nickname':				'alex_x',
				'sequence-name':					'Харухи Судзумия',
				'sequence-number':					1,
				'document-info-src-url':			'http://www.suzumiya.ru/v01t02',
				'document-info-id':					'956A7C50-2CBC-44C4-B80E-37A96F1B9561',
				'document-info-version':			'1.0',
			},
			'links': [
				'http://www.suzumiya.ru/v01t02-pro',
				'http://www.suzumiya.ru/v01t02-ch01',
				'http://www.suzumiya.ru/v01t02-ch02',
				'http://www.suzumiya.ru/v01t02-ch03',
				'http://www.suzumiya.ru/v01t02-ch04',
				'http://www.suzumiya.ru/v01t02-ch05',
				'http://www.suzumiya.ru/v01t02-ch06',
				'http://www.suzumiya.ru/v01t02-ch07',
				'http://www.suzumiya.ru/v01t02-epi',
				'http://www.suzumiya.ru/v01t02-author',
				'http://www.suzumiya.ru/v01t02-editor',
			],
		},
	'vol2': {
			'header': {
				'author-first-name':				'Нагару',
				'author-last-name':					'Танигава',
				'book-title':						'Вздохи Харухи Судзумии',
				'coverpage-image_link':				'http://www.suzumiya.ru/local--files/v02t01-images/v02t01_cover_cut.jpg',
				'translator-nickname':				'alex_x',
				'sequence-name':					'Харухи Судзумия',
				'sequence-number':					2,
				'document-info-src-url':			'http://www.suzumiya.ru/v02t02',
				'document-info-id':					'956A7C50-2CBC-44C4-B80E-37A96F1B9562',
				'document-info-version':			'1.0',
			},
			'links': [
				'http://www.suzumiya.ru/v02t02-pro',
				'http://www.suzumiya.ru/v02t02-ch01',
				'http://www.suzumiya.ru/v02t02-ch02',
				'http://www.suzumiya.ru/v02t02-ch03',
				'http://www.suzumiya.ru/v02t02-ch04',
				'http://www.suzumiya.ru/v02t02-ch05',
				'http://www.suzumiya.ru/v02t02-epi',
				'http://www.suzumiya.ru/v02t02-author',
			],
		},
	'vol3': {
			'header': {
				'author-first-name':				'Нагару',
				'author-last-name':					'Танигава',
				'book-title':						'Скука Харухи Судзумии',
				'coverpage-image_link':				'http://www.suzumiya.ru/local--files/v03t01-images/v03t01_cover_cut.jpg',
				'translator-nickname':				'alex_x',
				'sequence-name':					'Харухи Судзумия',
				'sequence-number':					3,
				'document-info-src-url':			'http://www.suzumiya.ru/v03t02',
				'document-info-id':					'956A7C50-2CBC-44C4-B80E-37A96F1B9563',
				'document-info-version':			'1.0',
			},
			'links': [
				'http://www.suzumiya.ru/v03t02-pro',
				'http://www.suzumiya.ru/v03t02-ch01',
				'http://www.suzumiya.ru/v03t02-ch02',
				'http://www.suzumiya.ru/v03t02-ch03',
				'http://www.suzumiya.ru/v03t02-ch04',
				'http://www.suzumiya.ru/v03t02-author',
			],
		},
	'vol4': {
			'header': {
				'author-first-name':				'Нагару',
				'author-last-name':					'Танигава',
				'book-title':						'Исчезновение Харухи Судзумии',
				'coverpage-image_link':				'http://www.suzumiya.ru/local--files/v04t01-images/v04t01_cover_cut.jpg',
				'translator-nickname':				'himself',
				'sequence-name':					'Харухи Судзумия',
				'sequence-number':					4,
				'document-info-src-url':			'http://www.suzumiya.ru/v04t01',
				'document-info-id':					'956A7C50-2CBC-44C4-B80E-37A96F1B9564',
				'document-info-version':			'1.0',
			},
			'links': [
				'http://www.suzumiya.ru/v04t01-pro',
				'http://www.suzumiya.ru/v04t01-ch01',
				'http://www.suzumiya.ru/v04t01-ch02',
				'http://www.suzumiya.ru/v04t01-ch03',
				'http://www.suzumiya.ru/v04t01-ch04',
				'http://www.suzumiya.ru/v04t01-ch05',
				'http://www.suzumiya.ru/v04t01-ch06',
				'http://www.suzumiya.ru/v04t01-epi',
				'http://www.suzumiya.ru/v04t01-author',
			],
		},
	'vol5': {
			'header': {
				'author-first-name':				'Нагару',
				'author-last-name':					'Танигава',
				'book-title':						'Увлечённость Харухи Судзумии',
				'coverpage-image_link':				'http://sos-dan.ru/images/book5.jpg',
				'translator-nickname':				'himself, zHz',
				'sequence-name':					'Харухи Судзумия',
				'sequence-number':					5,
				'document-info-src-url':			'http://www.suzumiya.ru/v05t01',
				'document-info-id':					'956A7C50-2CBC-44C4-B80E-37A96F1B9565',
				'document-info-version':			'1.0',
			},
			'links': [
				'http://www.suzumiya.ru/v05t01-ch01-pro',
				'http://www.suzumiya.ru/v05t01-ch01',
				'http://www.suzumiya.ru/v05t01-ch02-pro',
				'http://www.suzumiya.ru/v05t01-ch02',
				'http://www.suzumiya.ru/v05t01-ch03-pro',
				'http://www.suzumiya.ru/v05t03-ch03',
			],
		},
	'vol6': {
			'header': {
				'author-first-name':				'Нагару',
				'author-last-name':					'Танигава',
				'book-title':						'Тревога Харухи Судзумии',
				'coverpage-image_link':				'http://sos-dan.ru/images/book6.jpg',
				'translator-nickname':				'O-Kimi, himself, nomeno',
				'sequence-name':					'Харухи Судзумия',
				'sequence-number':					6,
				'document-info-src-url':			'http://www.suzumiya.ru/v04t01',
				'document-info-id':					'956A7C50-2CBC-44C4-B80E-37A96F1B9566',
				'document-info-version':			'1.0',
			},
			'links': [
				'http://www.suzumiya.ru/v06t01-ch01',
				'http://www.suzumiya.ru/v06t01-ch02',
				'http://www.suzumiya.ru/v06t01-ch03',
				'http://www.suzumiya.ru/v06t01-ch04',
				'http://www.suzumiya.ru/v06t01-ch05',
				'http://www.suzumiya.ru/v06t01-author',
			],
		},
		
	# from english
	'vol1a': {
			'header': {
				'author-first-name':				'Нагару',
				'author-last-name':					'Танигава',
				'book-title':						'Меланхолия Харухи Судзумии',
				'coverpage-image_link':				'http://www.suzumiya.ru/local--files/v01t01-images/v01t01_cover_cut.jpg',
				'translator-nickname':				'himself',
				'sequence-name':					'Харухи Судзумия',
				'sequence-number':					1,
				'document-info-src-url':			'http://www.suzumiya.ru/v01t01',
				'document-info-id':					'956A7C50-2CBC-44C4-B80E-37A96F1B9571',
				'document-info-version':			'1.0',
			},
			'links': [
				'http://www.suzumiya.ru/v01t01-pro',
				'http://www.suzumiya.ru/v01t01-ch01',
				'http://www.suzumiya.ru/v01t01-ch02',
				'http://www.suzumiya.ru/v01t01-ch03',
				'http://www.suzumiya.ru/v01t01-ch04',
				'http://www.suzumiya.ru/v01t01-ch05',
				'http://www.suzumiya.ru/v01t01-ch06',
				'http://www.suzumiya.ru/v01t01-ch07',
				'http://www.suzumiya.ru/v01t01-epi',
				'http://www.suzumiya.ru/v01t01-author',
				'http://www.suzumiya.ru/v01t01-editor',
			],
		},
	'vol2a': {
			'header': {
				'author-first-name':				'Нагару',
				'author-last-name':					'Танигава',
				'book-title':						'Причуды Харухи Судзумии',
				'coverpage-image_link':				'http://www.suzumiya.ru/local--files/v02t01-images/v02t01_cover_cut.jpg',
				'translator-nickname':				'himself',
				'sequence-name':					'Харухи Судзумия',
				'sequence-number':					2,
				'document-info-src-url':			'http://www.suzumiya.ru/v02t01',
				'document-info-id':					'956A7C50-2CBC-44C4-B80E-37A96F1B9572',
				'document-info-version':			'1.0',
			},
			'links': [
				'http://www.suzumiya.ru/v02t01-pro',
				'http://www.suzumiya.ru/v02t01-ch01',
				'http://www.suzumiya.ru/v02t01-ch02',
				'http://www.suzumiya.ru/v02t01-ch03',
				'http://www.suzumiya.ru/v02t01-ch04',
				'http://www.suzumiya.ru/v02t01-ch05',
				'http://www.suzumiya.ru/v02t01-epi',
				'http://www.suzumiya.ru/v02t01-author',
			],
		},
	'vol3a': {
			'header': {
				'author-first-name':				'Нагару',
				'author-last-name':					'Танигава',
				'book-title':						'Скука Харухи Судзумии',
				'coverpage-image_link':				'http://www.suzumiya.ru/local--files/v03t01-images/v03t01_cover_cut.jpg',
				'translator-nickname':				'alfred_h, himself, Helioz, zHz',
				'sequence-name':					'Харухи Судзумия',
				'sequence-number':					3,
				'document-info-src-url':			'http://www.suzumiya.ru/v03t01',
				'document-info-id':					'956A7C50-2CBC-44C4-B80E-37A96F1B9573',
				'document-info-version':			'1.0',
			},
			'links': [
				'http://www.suzumiya.ru/v03t01-pro',
				'http://www.suzumiya.ru/v03t01-ch01',
				'http://www.suzumiya.ru/v03t01-ch02',
				'http://www.suzumiya.ru/v03t01-ch03',
				'http://www.suzumiya.ru/v03t01-ch04',
				'http://www.suzumiya.ru/v03t01-author',
			],
		},


	'vol7': {
			'header': {
				'author-first-name':				'Нагару',
				'author-last-name':					'Танигава',
				'book-title':						'Интриги Харухи Судзумии',
				'coverpage-image_link':				'http://sos-dan.ru/images/book7.jpg',
				'translator-nickname':				'Lingvowiki',
				'sequence-name':					'Харухи Судзумия',
				'sequence-number':					7,
				'document-info-src-url':			'http://wiki.sos-dan.ru/w/%D0%A1%D1%83%D0%B4%D0%B7%D1%83%D0%BC%D0%B8%D1%8F_%D0%A5%D0%B0%D1%80%D1%83%D1%85%D0%B8/%D0%A0%D0%B0%D0%BD%D0%BE%D0%B1%D1%8D/7_%D1%82%D0%BE%D0%BC',
				'document-info-id':					'956A7C50-2CBC-44C4-B80E-37A96F1B9577',
				'document-info-version':			'1.0',
			},
			'links': [
				'http://wiki.sos-dan.ru/w/%D0%A1%D1%83%D0%B4%D0%B7%D1%83%D0%BC%D0%B8%D1%8F_%D0%A5%D0%B0%D1%80%D1%83%D1%85%D0%B8/%D0%A0%D0%B0%D0%BD%D0%BE%D0%B1%D1%8D/7_%D1%82%D0%BE%D0%BC/%D0%9F%D1%80%D0%BE%D0%BB%D0%BE%D0%B3_%28ru%29',
				'http://wiki.sos-dan.ru/w/%D0%A1%D1%83%D0%B4%D0%B7%D1%83%D0%BC%D0%B8%D1%8F_%D0%A5%D0%B0%D1%80%D1%83%D1%85%D0%B8/%D0%A0%D0%B0%D0%BD%D0%BE%D0%B1%D1%8D/7_%D1%82%D0%BE%D0%BC/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_1_(ru)'
				'http://wiki.sos-dan.ru/w/%D0%A1%D1%83%D0%B4%D0%B7%D1%83%D0%BC%D0%B8%D1%8F_%D0%A5%D0%B0%D1%80%D1%83%D1%85%D0%B8/%D0%A0%D0%B0%D0%BD%D0%BE%D0%B1%D1%8D/7_%D1%82%D0%BE%D0%BC/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_2_(ru)',
				'http://wiki.sos-dan.ru/w/%D0%A1%D1%83%D0%B4%D0%B7%D1%83%D0%BC%D0%B8%D1%8F_%D0%A5%D0%B0%D1%80%D1%83%D1%85%D0%B8/%D0%A0%D0%B0%D0%BD%D0%BE%D0%B1%D1%8D/7_%D1%82%D0%BE%D0%BC/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_3_(ru)',
				'http://wiki.sos-dan.ru/w/%D0%A1%D1%83%D0%B4%D0%B7%D1%83%D0%BC%D0%B8%D1%8F_%D0%A5%D0%B0%D1%80%D1%83%D1%85%D0%B8/%D0%A0%D0%B0%D0%BD%D0%BE%D0%B1%D1%8D/7_%D1%82%D0%BE%D0%BC/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_4_(ru)',
				'http://wiki.sos-dan.ru/w/%D0%A1%D1%83%D0%B4%D0%B7%D1%83%D0%BC%D0%B8%D1%8F_%D0%A5%D0%B0%D1%80%D1%83%D1%85%D0%B8/%D0%A0%D0%B0%D0%BD%D0%BE%D0%B1%D1%8D/7_%D1%82%D0%BE%D0%BC/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_5_(ru)',
				'http://wiki.sos-dan.ru/w/%D0%A1%D1%83%D0%B4%D0%B7%D1%83%D0%BC%D0%B8%D1%8F_%D0%A5%D0%B0%D1%80%D1%83%D1%85%D0%B8/%D0%A0%D0%B0%D0%BD%D0%BE%D0%B1%D1%8D/7_%D1%82%D0%BE%D0%BC/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_6_(ru)',
				'http://wiki.sos-dan.ru/w/%D0%A1%D1%83%D0%B4%D0%B7%D1%83%D0%BC%D0%B8%D1%8F_%D0%A5%D0%B0%D1%80%D1%83%D1%85%D0%B8/%D0%A0%D0%B0%D0%BD%D0%BE%D0%B1%D1%8D/7_%D1%82%D0%BE%D0%BC/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_7_(ru)',
				'http://wiki.sos-dan.ru/w/%D0%A1%D1%83%D0%B4%D0%B7%D1%83%D0%BC%D0%B8%D1%8F_%D0%A5%D0%B0%D1%80%D1%83%D1%85%D0%B8/%D0%A0%D0%B0%D0%BD%D0%BE%D0%B1%D1%8D/7_%D1%82%D0%BE%D0%BC/%D0%AD%D0%BF%D0%B8%D0%BB%D0%BE%D0%B3_(ru)',
				'http://wiki.sos-dan.ru/w/%D0%A1%D1%83%D0%B4%D0%B7%D1%83%D0%BC%D0%B8%D1%8F_%D0%A5%D0%B0%D1%80%D1%83%D1%85%D0%B8/%D0%A0%D0%B0%D0%BD%D0%BE%D0%B1%D1%8D/7_%D1%82%D0%BE%D0%BC/%D0%90%D0%B2%D1%82%D0%BE%D1%80%D1%81%D0%BA%D0%BE%D0%B5_%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D0%B5_(ru)',
			],
		},

}

"""
book = [
'http://192.168.102.127/~maliy/suzumia/v04t01-pro',
'http://192.168.102.127/~maliy/suzumia/v04t01-ch01',
'http://192.168.102.127/~maliy/suzumia/v04t01-ch02',
'http://192.168.102.127/~maliy/suzumia/v04t01-ch03',
'http://192.168.102.127/~maliy/suzumia/v04t01-ch04',
'http://192.168.102.127/~maliy/suzumia/v04t01-ch05',
'http://192.168.102.127/~maliy/suzumia/v04t01-ch06',
'http://192.168.102.127/~maliy/suzumia/v04t01-epi',
'http://192.168.102.127/~maliy/suzumia/v04t01-author',
]
"""

# header of fb2 file
h0 = '''<?xml version="1.0" encoding="UTF-8"?>
<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink">'''

# title of fb2 file
h1 = ''' <description>
  <title-info>
   <genre>sf</genre>
   <author>
    <first-name>%(author-first-name)s</first-name>
    <last-name>%(author-last-name)s</last-name>
   </author>
   <book-title>%(book-title)s</book-title>
   <date></date>
   <coverpage>
    <image l:href="#%(coverpage-image)s"/></coverpage>
   <lang>ru</lang>
   <src-lang>en</src-lang>
   <translator>
    <nickname>%(translator-nickname)s</nickname>
   </translator>
   <sequence name="%(sequence-name)s" number="%(sequence-number)d"/>
  </title-info>
  <document-info>
   <author>
    <first-name>%(author-first-name)s</first-name>
    <last-name>%(author-last-name)s</last-name>
  </author>
   <program-used>2fb2.py (© 2010 by Andrew Derevyagin)</program-used>
   <date value="%(document-info-date_value)s">%(document-info-date)s</date>
   <src-url>%(document-info-src-url)s</src-url>
   <id>%(document-info-id)s</id>
   <version>%(document-info-version)s</version>
   <history>
    <p>1.0 — created</p>
   </history>
  </document-info>
 </description>
'''

# get filename from url
def fileNameFromLink(link):
	return link.split('/')[-1]

# download image and resize
def image(link):
	ifn = fileNameFromLink(link)

	cmd = "rm -f ./%s;\nwget %s 2>&1"%(ifn, link)
	print cmd
	p = os.popen(cmd)
	for line in p.readlines():
		pass
		#if line.find('Saving to')>-1:
		#	ifn = line[line.find('`')+1:line.find("'")]

	im = Image.open(ifn)
	sz = 700, 700
	if im.size[0]>sz[0] or im.size[1]>sz[1]:
		im.thumbnail(sz, Image.ANTIALIAS)
		im.save(ifn, 'JPEG')
	return ifn

# get content between <tag>...</tag>
def content(data, tag):
	level = 1
	rv = 0
	d = data
	while level>0:
		a = d.find('</%s>'%tag)
		b = d.find('<%s'%tag)
		if a==-1:
			print 'break'
			return None
		if b==-1: b = a+1
		if a<b:
			rv += a+1
			level -= 1
		else:
			rv += b+1
			level += 1
		d = data[rv:]
	return data[:rv]

# get one chapter from suzumiya.ru
def chapterFromSuzumiyaRu(url, last_footer_id=0):
	title = None
	text = []
	images = []
	footers = []
	f = urllib.urlopen(url)
	data = f.read()
	host = 'http://www.suzumiya.ru/'
	k = data.find('id="page-title"')
	if k!=-1:
		tmp = data[k:]
		title = tmp[tmp.find('>')+1:tmp.find('</div>')].strip()
		print title
	k = data.find('id="page-content"')
	if k!=-1:
		# get main content
		tmp = content(data[k:], 'div')
		tmp = tmp[tmp.find('>')+1:]

		# split text & footnotes
		k = tmp.find('<div class="footnotes-footer"')

		# parse text
		txt = tmp[:k]
		txt = txt.replace('<p>', '')
		for _ in txt.split('</p>'):
			if len(text)>0:
				text.append('')
			for __ in _.split('<br />'):
				__ = __.strip()
				if len(__)>0:
					#replace footnote to '[footnote id="xx" /]'
					__ = re.sub(r'<sup class="footnoteref">.*?onclick="WIKIDOT\.page\.utils\.scrollToReference\(\'footnote-\d+\'\)">(\d+)</a></sup>', r'[footnote id="\1" /]', __.strip())
					#replace image to '[img src="link" /]'
					__ = re.sub(r'<a href="(.+?)"><img.+?/></a>', r'[img src="http://www.suzumiya.ru\1" /]', __)
					# remove another html tags
					__ = re.sub(r'\<[^>]*>', '', __)
					# one image on line
					idx = __.find('[img src=')
					while idx>-1:
						add = __[:idx].strip()
						if len(add)>0:
							text.append(add)
						link = __[idx+10:__[idx+10:].find('"')+idx+10]
						ifn = image(link)
						images.append(ifn)
						text.append(__[idx:idx+len(link)+14])
						__ = __[idx+len(link)+14:].strip()
						idx = __.find('[img src=')
					if len(__)>0:
						text.append(__)
					#print len(text[-1]), text[-1]

		# parse footnotes
		ft = tmp[k:]
		ft = ft.split('class="footnote-footer"')[1:]
		for _ in ft:
			tmp = content(_, 'div')
			k = tmp.find('</a>.')
			if k==-1:
				print 'Empty footnote "%s"'%f
				sys.exit(1)
			tmp = tmp[k+5:-1].strip()
			tmp = re.sub(r'\<[^>]*>', '', tmp)
			footers.append(tmp)
			print len(footers), footers[-1]

	f.close()
	return (title, text, images, footers)

# get one chapter from wiki.sos-dan.ru
def chapterFromWikiSOSdanRu(url, last_footer_id=0):
	title = None
	text = []
	images = []
	footers = []
	f = urllib.urlopen(url)
	data = f.read()
	host = 'http://www.suzumiya.ru/'
	k = data.find('id="firstHeading"')
	if k!=-1:
		tmp = data[k:]
		title = tmp[tmp.find('>')+1:tmp.find('</')].strip()
		title = re.sub(r'.*\/', '', title)
		title = re.sub(r'\(ru\)', '', title).strip()
		print title
	k = data.find('id="bodyContent"')
	if k!=-1:
		# get main content
		tmp = content(data[k:], 'div')
		tmp = tmp[tmp.find('<p>'):]

		# split text & footnotes
		k = tmp.find('<h2>')
		if k==-1:
			k = tmp.find('<h3>')

		# parse text
		txt = tmp[:k]
		txt = txt.replace('<p>', '')
		for _ in txt.split('</p>'):
			if len(text)>0:
				text.append('')
			for __ in _.split('<br />'):
				__ = __.strip()
				if len(__)>0:
					#replace footnote to '[footnote id="xx" /]'
					__ = re.sub(r'<sup [^>]*><a href=[^>]*>\[(\d+)\]</a></sup>', r'[footnote id="\1" /]', __)
					#replace image to '[img src="link" /]'
					idx = __.find('<div class="thumb')
					while idx>-1:
						if idx>0:
							# remove html tags and add
							add = re.sub(r'\<[^>]*>', '', __[:idx].strip())
							if len(add)>0:
								text.append(add)							
						tmp2 = content(__[idx+1:], 'div')
						tmp1 = tmp2[tmp2.find('src="')+6:]
						tmp1 = tmp1[:tmp1.find('"')]
						tmp1 = re.sub(r'thumb/', r'', tmp1)
						tmp1 = '/'.join(tmp1.split('/')[:-1])
						tmp1 = 'http://wiki.sos-dan.ru/'+tmp1
						ifn = image(tmp1)
						text.append('[img src="%s" /]'%ifn)
						__ =  __[idx+len(tmp2)+6:].strip()
						idx = __.find('<div class="thumb')
					# remove another html tags
					__ = re.sub(r'\<[^>]*>', '', __)
					if len(__)>0:
						text.append(__)

		# parse footnotes section
		ft = tmp[k:]
		ft = re.sub(r'\n', r'', ft)
		_ = re.search(r'<li id="[^"]+"><a href="[^"]+">[^<]+</a>(.+?)</li>', ft)
		while _:
			tmp = _.group(1).strip()
			ft = ft[ft.find(tmp):]
			tmp = re.sub(r'\<[^>]*>', '', tmp)
			footers.append(tmp)
			_ = re.search(r'<li id="[^"]+"><a href="[^"]+">[^<]+</a>(.+?)</li>', ft)
			print len(footers), footers[-1]

	f.close()
	return (title, text, images, footers)

# get one chapter by url
def chapter(url, last_footer_id=0):
	'''
		retrun (title, text(array of one line - paragraph), images, footers)
	'''

	rv = None
	if url.find('www.suzumiya.ru')>-1:
		rv = chapterFromSuzumiyaRu(url, last_footer_id)
	elif url.find('wiki.sos-dan.ru')>-1:
		rv = chapterFromWikiSOSdanRu(url, last_footer_id)
	return rv

# convert book to fb2
def convert2fb2(book):
	def isImage(l):
		if l.find(' ')==-1 and len(l)>4:
			if l[-4:].lower()=='.jpg':
				if os.path.exists(l):
					return True
		return False
	def escaping(l):
		rv =  l.replace("&", "&amp;")
		rv = rv.replace("<", "&lt;")
		rv = rv.replace(">", "&gt;")
		rv = rv.replace("\"", "&quot;")
		return rv

	book['header']['coverpage-image'] = image(book['header']['coverpage-image_link'])
	book['header']['document-info-date_value'] = time.strftime('%Y-%m-%d', time.localtime())
	book['header']['document-info-date'] = time.strftime('%d %B %Y', time.localtime())
	fb2_fn = '%02d %s(%s).fb2'%(book['header']['sequence-number'], book['header']['book-title'], book['header']['translator-nickname'].replace(', ', '_'))
	print fb2_fn
	fo = open(fb2_fn, 'w')
	fo.write('%s\n'%h0)
	fo.write(h1%book['header'])
	fo.write('<body>\n <title>\n  <p>%(author-first-name)s %(author-last-name)s</p>\n  <empty-line/>\n  <p>%(book-title)s</p>\n </title>\n'%book['header'])
	footnotes = []
	binarys = []
	last = ''
	sectionCount = 0
	footnotes_tmp = 0
	footnotes_retId = 1
	for bLink in book['links']:
		ch = chapter(bLink)
		if sectionCount>0:
			fo.write(' </section>\n') 
		footnotes_tmp = len(footnotes)
		fo.write(' <section>\n  <title>\n   <p>%s</p>\n  </title>\n'%ch[0])
		sectionCount += 1
		# line = paragraph
		for line in ch[1]:
			# line - image
			tmp = re.search(r'\[img src="(.+?)" /\]', line)
			if tmp:
				link = tmp.group(1)
				ifn = fileNameFromLink(link)
				binarys.append(ifn)
				fo.write('  <image l:href="#' + ifn + '" />\n')
				continue
			
			# line have footers
			footnote_return_add = ''
			tmp = re.search(r'\[footnote id="(\d+)" /\]', line)
			while tmp:
				fn_id = int(tmp.group(1))-1
				footnotes.append((ch[3][fn_id], footnotes_retId))
				if footnote_return_add=='':
					footnote_return_add = ' id="fn%d_ret"'%footnotes_retId
					footnotes_retId += 1
				idx = len(footnotes)
				link = '<a l:href="#fn_%d" type="note">[%d]</a>'%(idx,idx)
				line = line[:line.find('[footnote')] + link + line[line.find('/]')+2:]
				tmp = re.search(r'\[footnote id="(\d+)" /\]', line)
			if len(line)>0:
				fo.write('  <p%s>'%footnote_return_add)
				fo.write(line)
				fo.write('</p>\n')
			else:
				fo.write('  <empty-line/>\n')
	
	if sectionCount>0:
		fo.write(' </section>\n')
	fo.write('</body>\n')

	#write footnotes
	if len(footnotes)>0:
		fo.write('<body name="notes">\n')
		fo.write(u' <title>\n  <p>Footnotes</p>\n </title>\n')
		for i in range(len(footnotes)):
			n = footnotes[i][0]
			n = '<a l:href="#fn%d_ret" type="note">[%d]</a>%s'%(footnotes[i][1], i+1, n)
			idx = i+1
			fo.write(u' <section id="fn_%d">\n'%(idx))
			fo.write(u'  <p>')
			fo.write(n)
			fo.write(u'</p>\n </section>\n')
		fo.write('</body>\n')
		
	#write cover
	f = open(book['header']['coverpage-image'])
	data = binascii.b2a_base64(f.read())
	f.close()
	fo.write('<binary content-type="image/jpeg" id="' + book['header']['coverpage-image'] + '">%s</binary>\n'%data)

	#write binarys
	for bin in binarys:
		f = open(bin)
		data = binascii.b2a_base64(f.read())
		f.close()
		fo.write('<binary content-type="image/jpeg" id="' + bin + '">' + data + '</binary>\n')

	fo.write('</FictionBook>\n')
	fo.close()

def help():
	print 'Converting sites (suzumia.ru & sos-dan.ru) to fb2'
	print 'Usage: %s <key>'%sys.argv[0]
	print ' keys:'
	for key in sorted(presets.keys()):
		print '  %s\t- %s(%s %s) translated by: %s'%(key, presets[key]['header']['book-title'], presets[key]['header']['author-first-name'], presets[key]['header']['author-last-name'], presets[key]['header']['translator-nickname'])
	print
	print 'AUTHOR'
	print '  Writen by Andrey Derevyagin'
	print 'COPYRIGHT'
	print '  Copyright © 2010 Andrey Derevyagin'
	print 'BUGS'
	print '  If you feel you have found a bug  please email me 2derand@gmail.com'

#     ----------------- main section -----------------
if __name__=='__main__':
	if len(sys.argv)==2:
		if sys.argv[1]=='-h' or sys.argv[1]=='--help':
			help()
		elif presets.has_key(sys.argv[1]):
			convert2fb2(presets[sys.argv[1]])
		else:
			help()
	else:
		help()


