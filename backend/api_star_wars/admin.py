from django.contrib import admin

# Register your models here.
from .models import Director
from .models import Productor
from .models import Character
from .models import Movie
from .models import Planet

admin.site.register(Director)
admin.site.register(Productor)
admin.site.register(Character)
admin.site.register(Movie)
admin.site.register(Planet)
