from django.contrib import admin
from django.contrib.auth.models import User
from .models import Board, PublicBoard, Purpose, Tag, RTag, Rigor, Mood, Ban, BanType

# Register your models here.

admin.site.register(Board)
admin.site.register(PublicBoard)
admin.site.register(Purpose)
admin.site.register(Tag)
admin.site.register(RTag)
admin.site.register(Rigor)
admin.site.register(Mood)
admin.site.register(Ban)
admin.site.register(BanType)
