import os
import re
import sys
import urllib2
from xml.dom import minidom
from string import letters
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
	autoescape = True)

art_key = db.Key.from_path('ASCIIChan', 'arts')

def console(s):
	"""Writes an error message (s) to the console."""
	sys.stderr.write('%s\n' % s)

console(art_key)

class Handler(webapp2.RequestHandler):
  def write(self, *a, **kw):
  	self.response.write(*a, **kw)

  def render_str(self, template, **params):
  	t = jinja_env.get_template(template)
  	return t.render(params)

  def render(self, template, **kw):
  	self.write(self.render_str(template, **kw))

IP_URL = "http://api.hostip.info/?ip="
def get_coords(ip):
	#ip = "4.2.2.2"
	ip = "23.24.209.141"
	url = IP_URL + ip
	content = None
	try:
		content = urllib2.urlopen(url).read()
	except urllib2.URLError:
		return

	if content:
		d = minidom.parseString(content)
		coords = d.getElementsByTagName("gml:coordinates")
		if coords and coords[0].childNodes[0].nodeValue:
			lon, lat = coords[0].childNodes[0].nodeValue.split(',')
			return db.GeoPt(lat, lon)

GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=300x263&sensor=false&"
def gmaps_img(points):
	markers = '&'.join('markers=%s,%s' % (p.lat, p.lon)
						for p in points)
	return GMAPS_URL + markers

class Art(db.Model):
	title = db.StringProperty(required = True)
	art = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	coords = db.GeoPtProperty()

class MainPage(Handler):
	def render_front(self, error = '', title = '', art = ''):
		arts = db.GqlQuery(
			"""SELECT * FROM Art WHERE ANCESTOR IS :1 ORDER BY created LIMIT 10""", art_key)

		# prevents running the query multiple times
		arts = list(arts)

		# points = []
		# for a in arts:
		# 	if arts.coords:
		# 		points.append(a.coords)

		points = filter(None, (a.coords for a in arts))
		img_url = None
		if points:
			img_url = gmaps_img(points)

		self.render('front.html', title=title, art=art, error=error, arts=arts, img_url=img_url)

	def get(self):
		return self.render_front()

	def post(self):
		title = self.request.get('title')
		art = self.request.get('art')
		if title and art:
			p = Art(parent = art_key, title=title, art=art)
			coords = get_coords(self.request.remote_addr)
			if coords:
				p.coords = coords
			p.put()
			self.redirect('/')
		else:
			error = "we need both a title and some artwork!"
			self.render_front(error=error, title=title, art=art)

app = webapp2.WSGIApplication([('/', MainPage)], debug = True)
