#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lian'
__email__ = "liantian@188.com"


# Stdlib imports
import time

# Core Django imports
from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings


# Third-party app imports


# Imports from your apps
# from .models import Category
from .models import Post

# Create your models here.

PER_PAGE = getattr(settings, 'PER_PAGE', 10)
BLOG_TITLE = getattr(settings, 'BLOG_TITLE', "BLOG_TITLE")
BLOG_DESCRIPTION = getattr(settings, 'BLOG_DESCRIPTION', ["BLOG_DESCRIPTION"])


class BaseView(View):
    __doc__ = """修改了系统自带的View，加入一个setup（）的初始化函数"""

    def setup(self, request):
        self.response_dict = {}
        self.request = request
        pages = Post.objects.filter(type="page").all()
        # categories = Category.objects.all()
        # self.response_dict["categories"] = categories
        self.response_dict["pages"] = pages
        self.response_dict["PER_PAGE"] = PER_PAGE
        self.response_dict["BLOG_TITLE"] = BLOG_TITLE
        self.response_dict["BLOG_DESCRIPTION"] = BLOG_DESCRIPTION

    def dispatch(self, request, *args, **kwargs):
        self.setup(request)
        return View.dispatch(self, request, *args, **kwargs)

    @staticmethod
    def response_json(data):
        from .DjangoJSONEncoder import dumps
        return HttpResponse(dumps(data), content_type="application/json")

    @staticmethod
    def http_response(data, content_type="application/json"):
        return HttpResponse(data, content_type=content_type)

    def response(self, mimetype="text/html", template_file=None):
        return render_to_response(template_file,
                                  self.response_dict,
                                  content_type=mimetype,
                                  context_instance=RequestContext(self.request, processors=[]))

    @staticmethod
    def go(urlname, args):
        """用法 return self.go(urlname="wiki-view-page",args=(page_id,))"""
        return HttpResponseRedirect(reverse(urlname, args=args))

    @staticmethod
    def null_good():
        # 服务器成功处理了请求，但未返回任何内容。
        return HttpResponse(status=204)

    def go_to_referer(self):
        return HttpResponseRedirect(self.request.META['HTTP_REFERER'])


class IndexView(BaseView):
    def get(self, request):
        posts = Post.objects.filter(type="blog", status="publish").all()
        self.response_dict["posts"] = posts
        return self.response(template_file="index.html")


class PostView(BaseView):
    def get(self, request, year, month, day, url_slug):
        # self.response_dict["url_slug"] = url_slug
        post = Post.objects.filter(url_slug=url_slug).get()
        self.response_dict["post"] = post
        return self.response(template_file="post.html")
