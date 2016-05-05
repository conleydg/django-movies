from django.contrib import admin

from .models import Rater, Movies, Rating

admin.site.register(Rater)
admin.site.register(Movies)
admin.site.register(Rating)
