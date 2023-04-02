from django.db import models
from django.forms import ModelForm
from django.core.exceptions import ValidationError


#https://uk.indeed.com/career-advice/career-development/quotes-by-famous-authors
# Create your models here.
class Author(models.Model):
    first_name =models.CharField(max_length=30)
    last_name =models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Quotes(models.Model):
    quote = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quote } - {self.author}'

class QuotesForm(ModelForm):
    class Meta:
        model = Quotes
        fields = ['quote' , 'author']