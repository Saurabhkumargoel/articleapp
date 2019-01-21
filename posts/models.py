from django.db import models

# Create your models here.
class Catagory(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter type of article)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
		
		
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Article(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    
    article_text = models.TextField(max_length=1000, help_text='Article Text')
    catagory = models.ManyToManyField(Catagory, help_text='Select a catagory')
	
    date_of_creation = models.DateField(null=True, blank=True)
    
    def display_catagory(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(catagory.name for catagory in self.catagory.all()[:3])
    
    display_catagory.short_description = 'Catagory'
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('article-detail', args=[str(self.id)])
		
		
		
class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
		
