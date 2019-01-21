from django.shortcuts import render

# Create your views here.
from posts.models import Article, Author, Catagory

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_articles = Article.objects.all().count()

    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    context = {
        'num_articles': num_articles,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
	
from django.http import HttpResponseRedirect

from django.views import generic
class ArticleListView(generic.ListView):
	model =Article
	paginate_by = 2
	
class ArticleDetailView(generic.DetailView):
	model =  Article

class AuthorListView(generic.ListView):
	model =Author
	paginate_by = 2
	
class AuthorDetailView(generic.DetailView):
	model =  Author


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from posts.models import Article
from django.contrib.admin.views.decorators import staff_member_required
from braces import views

#@staff_member_required
class ArticleCreate(views.LoginRequiredMixin,views.StaffuserRequiredMixin,CreateView):
    model = Article
    val=Article.objects.all().filter(title='Lorem Ipsum1')
    fields = '__all__'

#@staff_member_required
class ArticleUpdate(views.LoginRequiredMixin,views.StaffuserRequiredMixin,UpdateView):
    model = Article
    fields = ['title',
		'author',
		'article_text',
		'catagory',
		'date_of_creation',]

#@staff_member_required
class ArticleDelete(views.LoginRequiredMixin,views.StaffuserRequiredMixin,DeleteView):
    model = Article
    success_url = reverse_lazy('articles')
'''
def add(request,pk,id =None):
    
    return HttpResponseRedirect(request.path_info)
	
def delete(request,pk,id =None):
    object = Article.objects.get(id=pk)
    object.delete()
    return HttpResponseRedirect(request.path_info)
'''