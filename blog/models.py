# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '$USER'
__email__ = "liantian@188.com"
# Stdlib imports

# Core Django imports

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.http import urlquote

# Third-party app imports
from djangae import fields
import markdown


# Imports from your apps
# from mysite.models import CommonModel


class Post(models.Model):
    date = models.DateTimeField(verbose_name=_(u"添加时间"))
    modified = models.DateTimeField(verbose_name=_(u"修改时间"), auto_now=True)
    title = models.CharField(verbose_name=_(u"标题"), max_length=255)
    content = models.TextField(verbose_name=_(u"正文"))
    content_less = models.TextField(verbose_name=_(u"简单正文"), blank=True)
    TYPE_CHOICES = (
        ('blog', _(u"博文")),
        ('page', _(u"页面")),
    )
    type = models.CharField(verbose_name=_(u"类型"), choices=TYPE_CHOICES, default="blog", max_length=255)
    STATUS_CHOICES = (
        ('new', _(u"新文章")),
        ('publish', _(u"已发布")),
    )
    status = models.CharField(verbose_name=_(u"状态"), choices=STATUS_CHOICES, default="new", max_length=255)

    url_slug = models.CharField(verbose_name=_(u"url_slug"), max_length=255, unique=True)

    def url_slug_safe(self):
        return urlquote(self.url_slug).encode("utf-8")

    def content_less_md(self):
        return markdown.markdown(self.content_less, extensions=['gfm'])

    def content_md(self):
        return markdown.markdown(self.content, extensions=['gfm'])

    # tags = ndb.StringProperty(repeated=True, indexed=False)
    # categories = ndb.StringProperty(indexed=False)

    class Meta:
        verbose_name = _(u"文章")
        verbose_name_plural = verbose_name
        ordering = ["-date"]
