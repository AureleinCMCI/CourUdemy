from django.contrib import admin

# Register your models here.
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom','ingrédient','vegetarienne','prix')
    search_fields = ['nom']
admin.site.register(Pizza, PizzaAdmin)