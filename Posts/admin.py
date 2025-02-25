from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')  # Admin panelinde listelenecek alanlar
    search_fields = ('title', 'content')  # Arama özelliği
