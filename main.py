 #!/bin/python
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import urllib, sys

from path_parse import path_parse
from page_compose import page_compose
from database_access import DatabaseAccess

db = DatabaseAccess("duh", "duh", "duh", "duh")

class Website(BaseHTTPRequestHandler):
	def do_GET(self):
		if "/beta" in self.path: # because for some reason, beta.cavej376.xyz did not work
			self.path = self.path[5:]
		
		action, content = path_parse(self.path) # first, we parse path and select method applicable
		content.database = db # then, we give content composer our database to work with
		content.compose() # afterwards, we compose content
		page = page_compose(content) # lastly, we put content into page
		self.send_response(content.err)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(page.encode("utf-8")) # and finally, send resulting page

ThreadingHTTPServer(("", 46667), Website).serve_forever()
