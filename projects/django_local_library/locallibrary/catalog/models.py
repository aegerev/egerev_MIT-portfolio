from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.function import Lower

# Create your models here.
''' The Genre Model'''
class Genre(models.model):
    name = models.CharField(max_length=200, 
                            unique=True, 
                            help_text="Need a book genre (Sci-Fi, Poetry, etc.) to operate! ")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])

class Meta:
    constraints = [
        UniqueConstraint(
            Lower('name'),
            name='genre_name_case_insensitive_unique',
            violation_error_message="Error Code 983: Case Insenstive Match - genre already exists"
        )
    ]

'''The Book Model'''
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    summary = models.TextField(max_length=1000,
                               help_text="Give me a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text='13-Character-Style <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
