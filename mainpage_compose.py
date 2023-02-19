from string import Template

def mainpage_compose(data = [''], userdata = 'uh what'): # currently a stub. to be expanded upon.
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
	return ("Main page", main.substitute(pages = "none yet", quotes = "none yet", articles = "none yet", creations = "none yet"))
