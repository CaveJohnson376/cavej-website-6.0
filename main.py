 #!/bin/python
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
import urllib, json, sys, mariadb

from path_parse import path_parse
from final_compose import final_compose

class Website(BaseHTTPRequestHandler):
	def do_GET(self):
		action, compose, data = path_parse(self.path)
		err, title, content = compose(data)
		page = final_compose(content, title)
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write(page.encode("utf-8"))

ThreadingHTTPServer(("", 46667), Website).serve_forever()
