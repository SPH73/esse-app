from django.contrib import admin

from .models import Portfolio, Bucket

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'user', 'created', 'updated')
    list_filter = ('created')
    search_fields = ('name', 'user')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('user',)
    date_hierarchy = ('created')
    ordering = ('user','created')
    
@admin.register(Bucket)
class BucketAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'portfolio', 'created', 'updated')
    list_filter = ('created')
    search_fields = ('name', 'portfolio')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = ('created')
    ordering = ('user','created')
    