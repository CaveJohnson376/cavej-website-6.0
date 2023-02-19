from string import Template

class BaseContent:
	is_composed = False # flip this to true once page is composed.
	err = 200 # error code. placeholder for now.
	title = "title" # page title. not necessarily content title. normal text only.
	content = "content" # page content. both HTML and normal text snippets are applicable.
	database = None # content database access class. must be set separately.
	
	def compose(self, path, userdata):
		# placeholder page is pre-composed; no compose required; set "is_composed" immediately.
		is_composed = True

class MainpageContent(BaseContent):
	
	pass
