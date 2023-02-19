from string import Template

class BaseContent:
	is_composed = False # flip this to true once page is composed.
	err = 200 # error code. placeholder for now.
	title = "title" # page title. not necessarily content title. normal text only.
	content = "content" # page content. both HTML and normal text snippets are applicable.
	request_path = "/stub"
	database = None # content database access class. must be set separately.
	
	def __init__(self, path):
		self.request_path = path
	
	def compose(self, userdata = 'uh what'):
		# placeholder page is pre-composed; no compose required; set "is_composed" immediately.
		self.is_composed = True

class ErrorPageContent(BaseContent):
	def __init__(self, path, err = 400):
		self.request_path = path
		self.err = err
	
	def compose(self, userdata = 'uh what'):
		self.title = "An error occured."
		self.content = Template("Server could not process your request for one reason or another.<br>Request path: $path<br>Returned error:$err").substitute(path = self.request_path, err = self.err)
		self.is_composed = True

# class for generating main page contents
class MainPageContent(BaseContent):
	def compose(self, userdata = 'uh what'): # currently a stub. to be expanded upon.
		self.title = "Main Page"
		main = Template(open('mainpage_templates/main.html', 'r').read())
		# TODO: add $pages, $articles, $creations and $quotes tags
	
		# TODO: add page button, quote block, article and creation preview templates, as well as tags for them
		# tags for page buttons:
		# 	- $title
		# tags for quote block:
		# 	- $num
		#	- $content
		# 	- $timestamp
		# tags for article preview:
		# 	- $title
		# 	- $description
		# 	- $imagelink
		# 	- $authorname
		# 	- $timestamp
		# tags for creation preview:
		# 	- $title
		# 	- $shortdesc
		# 	- $imagelink
		# 	- $authorname
		# 	- $timestamp
		# 	- $rating
		
		# TODO: add database integration
		self.content = main.substitute(pages = "none yet", quotes = "none yet", articles = "none yet", creations = "none yet")
		self.is_composed = True
	pass
