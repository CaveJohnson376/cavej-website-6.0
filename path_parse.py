from mainpage_compose import mainpage_compose

def err_placeholder_compose(data = [''], userdata = "uh what"):
	return ("critical error","something went horribly wrong. i cannot find what you are looking for!")

def path_parse(path = "/"):
	action = "return_page"
	compose = err_placeholder_compose
	post_path = ['']
	match path[1:].split("/"):
		case ['' | 'home' | 'main', *the_rest]:
			compose = mainpage_compose
			post_path = the_rest
		case other:
			post_path = other
	
	return (action, compose, post_path)
