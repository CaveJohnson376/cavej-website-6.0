import content as Composers

def path_parse(path = "/"):
	action = "return_page"
	content_composer = Composers.ErrorPageContent(path, 200)
	match path[1:].split("/"):
		case ['' | 'home' | 'main']:
			content_composer = Composers.MainPageContent(path)
		case other:
			action = "error"
			content_composer = Composers.ErrorPageContent(path, 404)
	
	return (action, content_composer)
