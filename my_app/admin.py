from django.contrib import admin

# Register your models here.

from .models import Text
from .models import Map
from .models import Weapon
admin.site.register(Text)
admin.site.register(Map)
admin.site.register(Weapon)