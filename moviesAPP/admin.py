# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Movie,MovieDetails

admin.site.register(Movie)
admin.site.register(MovieDetails)


# Register your models here.
