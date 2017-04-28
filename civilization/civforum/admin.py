from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)

class PublicBoardAdmin(admin.ModelAdmin):
    list_display = ('board',)
    
# Register your models here.

admin.site.register(Board, BoardAdmin)
admin.site.register(PublicBoard, PublicBoardAdmin)
admin.site.register(Purpose)
admin.site.register(Tag)
admin.site.register(RTag)
admin.site.register(Rigor)
admin.site.register(Mood)
admin.site.register(Ban)
admin.site.register(BanType)

# Debug

admin.site.register(Thread)
