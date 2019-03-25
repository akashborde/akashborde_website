from django.shortcuts import render
#from django.http import HttpResponse

#dummy data
#list of dictionaries
#each dictionary is associated with a post
posts = [
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'August 27, 2018'
	},
	{
		'author': 'Aba',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'August 28, 2018'
	}
]

# Create your views here.


def home(request):
	#make a dictionary
	#pass in the stuff made at the top

	#keys of this context is what is going to be accessible from this template.

	#this context is fed to the HTML, which formats the page
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)
	#context passes the data within the template
	#return HttpResponse('<h1>Blog Home</h1>') #returns the header blog home

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})



#handles the traffic from blog's homepage
#will take a request which will be implemented later 
#has what the user will see when they're sent to this route

#this comes from blog.urls.py

#gotta load the templates somehow
#render it, pass to HttpResponse
#django does this in one step -- render
