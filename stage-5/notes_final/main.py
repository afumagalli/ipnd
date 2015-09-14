#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import cgi
import urllib
import urllib2
import webapp2
import jinja2
from xml.dom import minidom
from string import letters

from google.appengine.api import users
from google.appengine.ext import ndb

from content import STAGES

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(
	loader = jinja2.FileSystemLoader(template_dir),
	extensions = ['jinja2.ext.autoescape'],
	autoescape = True)
prev = "None"

DEFAULT_WALL = 'Public'

def wall_key(wall_name = DEFAULT_WALL):
	return ndb.Key('Wall', wall_name)

class Author(ndb.Model):
	identity = ndb.StringProperty(indexed=True)
	name = ndb.StringProperty(indexed=False)
	email = ndb.StringProperty(indexed=False)

class Post(ndb.Model):
	author = ndb.StructuredProperty(Author)
	content = ndb.StringProperty(indexed=False)
	date = ndb.DateTimeProperty(auto_now_add=True)
	coords = ndb.GeoPtProperty()

IP_URL = "http://ip-api.com/xml/"
def get_coords(ip):
	url = IP_URL + ip
	content = None
	try:
		content = urllib2.urlopen(url).read()
	except urllib2.URLError:
		return
	if content:
		d = minidom.parseString(content)
		coords = d.getElementsByTagName("status")[0].childNodes[0].nodeValue
		if coords == "success":
			lat = d.getElementsByTagName("lat")[0].childNodes[0].nodeValue
			lon = d.getElementsByTagName("lon")[0].childNodes[0].nodeValue
			return ndb.GeoPt(lat, lon)
		return
	return

GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&"
def gmaps_img(points):
	markers = '&'.join('markers=%s,%s' % (p.lat, p.lon) for p in points)
	return GMAPS_URL + markers

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **kw):
		t = jinja_env.get_template(template)
		return t.render(kw)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class NotesHandler(Handler):
	def get(self):
		self.render("notes.html", stages = STAGES, page_name = "notes")
		wall_name = DEFAULT_WALL
		posts_query = Post.query(ancestor = wall_key(wall_name)).order(-Post.date)
		posts =  posts_query.fetch()
		posts_list = list(posts)
		user = users.get_current_user()
		global prev

		if user:
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
			user_name = user.nickname()
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login with Google'
			user_name = 'Anonymous Poster'

		points = []
		for p in posts_list:
			if p.coords:
				points.append(p.coords)

		img_url = None
		if points:
			img_url = gmaps_img(points)

		sign_query_params = urllib.urlencode({'wall_name': wall_name})
		self.render("comments.html", sign_query_params = sign_query_params,
					wall_name = wall_name, user_name = user_name, url = url, user = user,
					url_linktext = url_linktext, posts = posts, prev = prev, img_url = img_url)

class CourseHandler(Handler):
	def get(self, stage_number):
		self.render("course.html", stage_number=int(stage_number), stage=STAGES[int(stage_number)-1], page_name="notes")

class PostWall(webapp2.RequestHandler):
	def post(self):
		wall_name = DEFAULT_WALL
		post = Post(parent = wall_key(wall_name))
		user = users.get_current_user()
		global prev

		if user:
			post.author = Author(
				identity = user.user_id(),
				name = user.nickname(),
				email = user.email())
		else:
			post.author = Author(
				name = 'Anonymous',
				email = 'anonymous@anonymous.com')

		post.content = self.request.get('content')
		if post.content:
			coords = get_coords(self.request.remote_addr)
			if coords:
				post.coords = coords
			post.put()
			prev = "Success"
		else:
			prev = "Error"
		self.redirect('/#wall')

app = webapp2.WSGIApplication([
	('/', NotesHandler),
	(r'/(\d+)/', CourseHandler),
	('/sign', PostWall)
], debug=True)
