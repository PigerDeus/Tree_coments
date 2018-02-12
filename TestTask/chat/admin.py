from django.contrib import admin

# Register your models here.
from .models import Comment, SubComment

admin.site.register(Comment)
admin.site.register(SubComment)
