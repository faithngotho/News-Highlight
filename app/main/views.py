from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Sources

#views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	sources = get_sources('business')
	title = "News Highlighter"

	return render_template('index.html',title = title, sources = sources)

@main.route('/articles/<id>')
def articles(id):
	'''
	view articles page
	'''
	
	return render_template('articles.html',title= title, articles = articles)
