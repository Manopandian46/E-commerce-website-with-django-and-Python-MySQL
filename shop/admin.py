from atexit import register
from django.contrib import admin
from .models import *


admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)
