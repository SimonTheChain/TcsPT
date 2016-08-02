from django.contrib import admin
from .models import Video, Audio, Subtitle, Image, Note


admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Subtitle)
admin.site.register(Image)
admin.site.register(Note)
