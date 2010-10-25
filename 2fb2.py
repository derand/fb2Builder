#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re, binascii

header5 = {
	'author-first-name':	'Нагару',
	'author-last-name':		'Танигава',
	'book-title':			'Увлечённость Харухи Судзумии',
	'coverpage-image':		'book5.jpg',
	'translator-nickname':	'himself',
	'sequence-name':		'Харухи Судзумия',
	'sequence-number':		5,
	'document-info-author-nickname':	'Adalar',
	'document-info-program-used':		'2fb2.py',
	'document-info-date':				'26 August 2010',
	'document-info-date_value':			'2010-08-26',
	'document-info-src-url':			'http://www.suzumiya.ru/v05t01',
	'document-info-id':					'956A7C50-2CBC-44C4-B80E-37A96F1B9557',
	'document-info-version':			'1.0',
}

header = {
	'author-first-name':	'Нагару',
	'author-last-name':		'Танигава',
	'book-title':			'Тревога Харухи Судзумии',
	'coverpage-image':		'book6.jpg',
	'translator-nickname':	'himself',
	'sequence-name':		'Харухи Судзумия',
	'sequence-number':		6,
	'document-info-author-nickname':	'Adalar',
	'document-info-program-used':		'2fb2.py',
	'document-info-date':				'26 August 2010',
	'document-info-date_value':			'2010-08-26',
	'document-info-src-url':			'http://www.suzumiya.ru/v06t01',
	'document-info-id':					'956A7C50-2CBC-44C4-B80E-37A96F1B9558',
	'document-info-version':			'1.0',
}

h0 = '''<?xml version="1.0" encoding="UTF-8"?>\n<FictionBook xmlns="http://www.gribuser.ru/xml/fictionbook/2.0" xmlns:l="http://www.w3.org/1999/xlink">'''

h1 = ''' <description>\n  <title-info>\n   <genre>sf</genre>\n   <author>\n    <first-name>%(author-first-name)s</first-name>\n    <last-name>%(author-last-name)s</last-name>\n   </author>\n   <book-title>%(book-title)s</book-title>\n   <date></date>\n   <coverpage>\n    <image l:href="#%(coverpage-image)s"/></coverpage>\n   <lang>ru</lang>\n   <src-lang>en</src-lang>\n   <translator>\n    <nickname>%(translator-nickname)s</nickname>\n   </translator>\n   <sequence name="%(sequence-name)s" number="%(sequence-number)d"/>\n  </title-info>\n  <document-info>\n   <author>\n    <first-name>%(author-first-name)s</first-name>\n    <last-name>%(author-last-name)s</last-name>\n   </author>\n   <program-used>%(document-info-program-used)s</program-used>\n   <date value="%(document-info-date_value)s">%(document-info-date)s</date>\n   <src-url>%(document-info-src-url)s</src-url>\n   <id>%(document-info-id)s</id>\n   <version>%(document-info-version)s</version>\n   <history>\n    <p>1.0 — создание файла</p>\n   </history>\n  </document-info>\n </description>\n'''

def convert2fb2(fn):
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

	print fn
	fb2_fn = '.'.join(fn.split('.')[:-1])+'.fb2'
	print fb2_fn
	fo = open(fb2_fn, 'w')
	fo.write('%s\n'%h0)
	fo.write(h1%header)
	fo.write('<body>\n <title>\n  <p>%(author-first-name)s %(author-last-name)s</p>\n  <p>%(book-title)s</p>\n </title>\n'%header)
	fi = open(fn)
	footnotes = []
	binarys = []
	last = ''
	sectionCount = 0
	footnotes_tmp = 0
	footnotes_retId = 1
	# тип сносок:
	#  0 - через всю книгу отдельным тегом 
	#  1 - в конце каждой главы
	#  2 - через всю книгу отдельным тегом со ссылкой назад
	footnotes_type = 2
	for line in fi:
		line = line.strip()
		#print len(line), line
		if len(line):
			if line.find('<title>')>-1:
				ttt = re.sub(r'\<title\>', '', line)
				if sectionCount>0:
					if footnotes_type==1:
						for i in range(footnotes_tmp, len(footnotes)):
							print footnotes[i][1], footnotes[i][0]
							'''<p id="fn1"><a l:href="#fn1_ret" type="note">[1]</a>текст</p>'''
							fo.write('   <empty-line/>\n   <p id="fn_%d"><a l:href="#fn%d_ret" type="note">[%d]</a>%s</p>\n'%(i+1, footnotes[i][1], i+1, footnotes[i][0]))
					fo.write(' </section>\n')
				print ttt
				footnotes_tmp = len(footnotes)
				fo.write(' <section>\n  <title><p>%s</p></title>'%ttt)
				sectionCount += 1
			else:
				if isImage(line):
					print 'image: "%s"'%line
					binarys.append(line)
					fo.write('<image l:href="#' + line + '" />\n')
				else:
					line = escaping(line)
					#...<footnote>...</footnote>...
					footnote_return_add = ''
					while line.find('&lt;footnote&gt;')!=-1:
						tmp = re.search(r'&lt;footnote&gt;(.+?)&lt;/footnote&gt;', line)
						if tmp:
							footnotes.append((tmp.group(1), footnotes_retId))
							if footnote_return_add=='':
								footnote_return_add = ' id="fn%d_ret"'%footnotes_retId
								footnotes_retId += 1
							idx = len(footnotes)
							tmp = '<a l:href="#fn_%d" type="note">[%d]</a>'%(idx,idx)
							line = line[:line.find('&lt;footnote&gt;')]+tmp+line[line.find('&lt;/footnote&gt;')+17:]
							#print 'footnote: %d'%idx, footnotes[-1][0]
						else:
							break
					fo.write('  <p%s>'%footnote_return_add)
					fo.write(line)
					fo.write('</p>\n')

		last = line
	if sectionCount>0:
		fo.write(' </section>\n')
	fi.close()
	fo.write('</body>\n')

	#write footnotes
	if (footnotes_type==0 or footnotes_type==2) and len(footnotes)>0:
		fo.write('<body name="notes">\n')
		fo.write(u' <title>\n  <p>Footnotes</p>\n </title>\n')
		for i in range(len(footnotes)):
			n = footnotes[i][0]
			if footnotes_type==2:
				n = '<a l:href="#fn%d_ret" type="note">[%d]</a>%s'%(footnotes[i][1], i+1, n)
			idx = i+1
			if footnotes_type==0:
				fo.write(u' <section id="fn_%d">\n  <title>\n   <p>%d</p>\n  </title>\n'%(idx,idx))
			elif footnotes_type==2:
				fo.write(u' <section id="fn_%d">\n'%(idx))
			fo.write(u'  <p>')
			fo.write(n)
			fo.write(u'</p>\n </section>\n')
		fo.write('</body>\n')
		
	#write cover
	f = open(header['coverpage-image'])
	data = binascii.b2a_base64(f.read())
	f.close()
	fo.write('<binary content-type="image/jpeg" id="' + header['coverpage-image'] + '">%s</binary>\n'%data)

	#write binarys
	for bin in binarys:
		f = open(bin)
		data = binascii.b2a_base64(f.read())
		f.close()
		fo.write('<binary content-type="image/jpeg" id="' + bin + '">' + data + '</binary>\n')

	fo.write('</FictionBook>\n')
	fo.close()

if len(sys.argv)==2:
	convert2fb2(sys.argv[1])
	

