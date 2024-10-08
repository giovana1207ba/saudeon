from django.contrib import admin
from .models import *

admin.site.register(CustomUser)

admin.site.register(Posto)
admin.site.register(Area)
admin.site.register(Medico)
admin.site.register(Consulta)

admin.site.register(Index)
admin.site.register(Sobre)