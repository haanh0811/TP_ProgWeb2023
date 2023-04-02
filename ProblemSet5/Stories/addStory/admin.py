from django.contrib import admin
from .models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name')

class QuotesAdmin(admin.ModelAdmin):
    list_display = ('id','quote','author')

admin.site.register(Author,AuthorAdmin)
admin.site.register(Quotes,QuotesAdmin)