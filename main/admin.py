from django.contrib import admin
from main.models import *
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display=('email', 'sent_at')

admin.site.register(Client, ClientAdmin)

admin.site.register(Category)
admin.site.register(Meals)