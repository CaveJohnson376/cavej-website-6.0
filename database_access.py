import json
# currently a stub that uses noSQL JSON-based "database" to imitate normal database
# 

class DatabaseAccess:
	addr = "localhost"
	user = "db"
	pswd = "password"
	dbnm = "database"
	
	#TODO: remove this
	tempdata = {}
	
	def __init__(self, addr, user, pswd, dbnm):
		self.addr = addr
		self.user = user
		self.pswd = pswd
		self.dbnm = dbnm
		
		#TODO: add actual database integration code here instead of this JSON abominaton
		f = open('placeholderdb.json', 'r')
		self.tempdata = json.loads(f.read())
	
	def get_article_list(self, amount, startwith = 0, sort = "arbitrary"):
		# sort types: arbitrary, title, date, (later on) author_name/ID

		articles = self.tempdata['articles']
		match sort:
			case 'arbitrary':
				articles = sorted(articles, key=lambda d: d['id'])
			case 'title':
				articles = sorted(articles, key=lambda d: d['title'])
			case 'date':
				articles = sorted(articles, key=lambda d: d['timestamp'])
		if amount:
			return articles[startwith:amount + startwith]
		else:
			return articles[startwith:]
	
	def get_article_by_id(self, art_id):
		articles = self.tempdata['articles']
		filtered_articles = list(filter(lambda article: article['id'] == art_id, articles))
		article = {}
		if len(filtered_articles) < 1:
			article = {
				"id":-1,
				"title":"missing article",
				"author":"none",
				"description":"article was not found",
				"timestamp":0,
				"content":"You are in a very strange place. There is no article here!"
			}
		else:
			article = filtered_articles[0]
		
		return article



		
