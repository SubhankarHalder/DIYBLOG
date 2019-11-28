from django.shortcuts import render
from blog.models import Blog, BlogAuthor, BlogComment
from django.views import generic

# Create your views here.

def index(request):
    """View function for homepage of the site"""

    # Generate counts of blog posts and blog authors

    num_blogs = Blog.objects.all().count()
    num_authors = BlogAuthor.objects.count()

    context = {
            'num_blogs' : num_blogs,
            'num_authors' : num_authors,
            }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context = context)

class BlogListView(generic.ListView):
    model = Blog

class BlogDetailView(generic.DetailView):
    model = Blog
