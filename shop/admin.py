from django.contrib import admin
from .models import Review,Business,ContactInfo,Media,Category

# Register your models here.
admin.site.register(Review)
admin.site.register(Business)
admin.site.register(ContactInfo)
admin.site.register(Media)
admin.site.register(Category)