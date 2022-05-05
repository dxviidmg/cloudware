from django.contrib import admin

from .models import Address, Quote


admin.site.register(Address)
admin.site.register(Quote)