
from django.contrib import admin

from .models import Note,User,TipoDeNota

admin.site.register(User)
admin.site.register(Note)
admin.site.register(TipoDeNota)

