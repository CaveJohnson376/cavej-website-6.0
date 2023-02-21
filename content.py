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
	ppath = []
	def __init__(self, path, parsedpath, err = 400):
		self.request_path = path
		self.ppath = parsedpath
		self.err = err
	
	def compose(self, userdata = 'uh what'):
		self.title = "An error occured."
		self.content = Template("Server could not process your request for one reason or another.<br>Request path: $path<br>Parsed path: $ppath<br>Returned error:$err").substitute(path = self.request_path, ppath = self.ppath, err = self.err)
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
		article_template = Template(open('mainpage_templates/article_preview.html', 'r').read())
		articles_list = self.database.get_article_list(10, 0, "date")[::-1]
		articles_str = ''
		for article in articles_list:
			articles_str += article_template.substitute(
					articleid = article["id"],
					title = article["title"],
					authorname = article["author"],
					imglink = article["imgurl"],
					timestamp = article["timestamp"],
					desc = article["description"]
			)
		
		# tags for creation preview:
		# 	- $title
		# 	- $shortdesc
		# 	- $imagelink
		# 	- $authorname
		# 	- $timestamp
		# 	- $rating
		
		# TODO: add database integration
		self.content = main.substitute(pages = "none yet", quotes = "none yet", articles = articles_str, creations = "none yet")
		self.is_composed = True
	pass

class ArticlePageContent(BaseContent):
	def compose(self, userdata = 'uh what'):
		article_id = int(self.request_path[9:])
		article_data = self.database.get_article_by_id(article_id)
		article_template = Template(open('templates/article_template.html', 'r').read())
		self.title = 'Article: ' + article_data['title']
		self.content = article_template.substitute(
				imglink = article_data['imgurl'],
				title = article_data['title'],
				authorname = article_data['author'],
				timestamp = article_data['timestamp'],
				content = article_data['content'].replace('\n', '<br>')
		)
		self.is_composed = True
		
		
		
		
		
		
		
		
		
		
