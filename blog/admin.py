#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lian'
__email__ = "liantian@188.com"

# Stdlib imports


# Core Django imports
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Third-party app imports


# Imports from your apps
from .models import Post


# from .models import Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'status')


# Register your models here.
admin.site.register(Post, PostAdmin)
# admin.site.register(Category)
