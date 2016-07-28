from django.contrib import admin
from .models import Asset, ImageAsset, AssetTest


admin.site.register(Asset)
admin.site.register(ImageAsset)
admin.site.register(AssetTest)
