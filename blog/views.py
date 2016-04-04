#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lian'
__email__ = "liantian@188.com"

# Stdlib imports


# Core Django imports

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

# Third-party app imports


# Imports from your apps

from .models import Post

# Create your models here.

BLOG_TITLE = u"LIANTIAN'S LOG"
BLOG_DESCRIPTION = [
    "\xe8\x99\x9b\xe5\x81\xbd\xe8\xa1\x97\xe8\xa7\x92\xef\xbc\x8c\xe6\x9c\x89\xe4\xbd\xa0\xe5\xbe\xae\xe7\xac\x91\xe2\x80\xa6",
    "\xe6\xb0\xb4\xe5\xba\x95\xe6\xbc\xb8\xe4\xb9\xbe\xef\xbc\x8c\xe6\x9c\x88\xe6\xbc\xb8\xe6\xbb\xbf\xe2\x80\xa6",
    "\xe9\xab\x98\xe7\x89\x86\xe4\xb9\x8b\xe5\x85\xa7\xef\xbc\x8c\xe5\xa4\xb1\xe8\x80\x8c\xe8\xa4\x87\xe5\xbe\x97\xe2\x80\xa6",
    "\xe6\xb7\xba\xe7\x9c\xa0\xe4\xb8\x80\xe5\xa4\xa2\xef\xbc\x8c\xe4\xb8\x8d\xe6\x9b\xbe\xe9\x86\x89\xe9\x85\x92\xe2\x80\xa6",
    "\xe4\xba\x94\xe6\x9c\x88\xe9\x9b\xa8\xe4\xb8\xad\xef\xbc\x8c\xe6\xa2\x94\xe5\xad\x90\xe8\x8a\xb1\xe9\xa6\x99\xe2\x80\xa6",
    "\xe8\x83\x8c\xe5\x8f\x9b\xe7\x9a\x84\xe8\xa8\x98\xe6\x86\xb6\xef\xbc\x8c\xe6\x98\xaf\xe7\x90\xa5\xe7\x8f\x80\xe8\x89\xb2\xe7\x9a\x84\xe5\xbe\xae\xe7\xac\x91\xe2\x80\xa6",
]


def index(request):
    response_dict = {}
    # response_dict["path"] = request.path
    response_dict["BLOG_DESCRIPTION"] = BLOG_DESCRIPTION
    response_dict["pages"] = Post.objects.filter(type="page").all()
    response_dict["posts"] = Post.objects.filter(type="blog", status="publish").all()
    return render_to_response("index.html",
                              response_dict,
                              content_type="text/html",
                              context_instance=RequestContext(request, processors=[]))


def post(request, year, month, day, url_slug):
    response_dict = {}
    # response_dict["path"] = request.path
    response_dict["BLOG_DESCRIPTION"] = BLOG_DESCRIPTION
    response_dict["pages"] = Post.objects.filter(type="page").all()
    response_dict["post"] = Post.objects.filter(url_slug=url_slug).get()
    response_dict["url_slug"] = url_slug
    return render_to_response("post.html",
                              response_dict,
                              content_type="text/html",
                              context_instance=RequestContext(request, processors=[]))


@cache_page(60 * 60)
def sitemap(request):
    response_dict = {}
    response_dict["posts"] = Post.objects.all()
    return render_to_response("sitemap.xml",
                                response_dict,
                                content_type="text/xml",
                                context_instance=RequestContext(request, processors=[]))