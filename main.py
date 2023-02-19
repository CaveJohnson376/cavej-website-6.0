 #!/bin/python
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import urllib, json, sys

from path_parse import path_parse
from page_compose import page_compose

class Website(BaseHTTPRequestHandler):
	def do_GET(self):
		action, content = path_parse(self.path)
		content.compose()
		page = page_compose(content)
		self.send_response(content.err)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(page.encode("utf-8"))

ThreadingHTTPServer(("", 46667), Website).serve_forever()
