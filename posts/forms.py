from django import ModelForm
    
from posts.models import Article

class RenewBookModelForm(ModelForm):
	pass
    class Meta:
        model = Article
        fields = [		
		'title',
		'author',
		'article_text',
		'catagory'
		'date_of_creation',
		]