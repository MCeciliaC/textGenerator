from django.contrib import admin
from .models import Select, Question, Greeting

# Register your models here.
admin.site.register(Select)
admin.site.register(Question)
admin.site.register(Greeting)
