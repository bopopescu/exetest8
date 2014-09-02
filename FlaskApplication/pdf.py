from flask import Flask, render_template
from flask import request, redirect


rule = request.url_rule
print rule

# import urllib2
# 
# data = {
#    'apikey': 'ChRWwwQst7uT',
#    'url': 'http://www.google.com'
# }
# requesturl = 'http://api.htm2pdf.co.uk/urltopdf?apikey={apikey}&url={url}'.format(**data)
# result = urllib2.urlopen(requesturl)
# localFile = open('mypdf.pdf', 'w')
# localFile.write(result.read())
# localFile.close()