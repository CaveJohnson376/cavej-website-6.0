from string import Template

# this function
# 1. takes all the fancy framing, header and footer file
# 2. stuffs it with title and content
# 3. gives back to main script

def final_compose(content = "missing content. if you see this - report to administrator.", title = "[no title]", userinfo = "uh what"):
	t = Template(open('base.html', 'r').read())
	# TODO: add discord and platform-specific stuff insertion
	return t.substitute(content = content, title = title)
