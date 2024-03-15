from django.contrib import admin
from .models import Video, Like, Category, Subcategory

admin.site.register(Video)
admin.site.register(Like)
admin.site.register(Category)
admin.site.register(Subcategory)
