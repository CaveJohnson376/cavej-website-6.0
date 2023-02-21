import content as Composers

def path_parse(path = "/"):
	action = "return_page"
	content_composer = Composers.ErrorPageContent(path, 200)
	match path[1:].split("/"):
		case ['' | 'home' | 'main', *_]:
			content_composer = Composers.MainPageContent(path)
		case ['article', *_]:
			content_composer = Composers.ArticlePageContent(path)
		case other:
			action = "error"
			content_composer = Composers.ErrorPageContent(path, other, 404)
	
	return (action, content_composer)
