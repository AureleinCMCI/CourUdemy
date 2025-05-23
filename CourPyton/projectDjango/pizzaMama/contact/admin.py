from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email','password')  # Colonnes affichées dans la liste
    search_fields = ('nom', 'prenom', 'email','password') # Champs de recherche

admin.site.register(Contact, ContactAdmin)
