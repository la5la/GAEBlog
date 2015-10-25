#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lian'
__email__ = "liantian@188.com"


# Stdlib imports
import uuid

# Core Django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Third-party app imports


# Imports from your apps


# Create your models here.

class CommonModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    db_created = models.DateTimeField(auto_now_add=True, verbose_name=_("创建日期"))
    db_modified = models.DateTimeField(auto_now=True, verbose_name=_("修改日期"))
    db_uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __unicode__(self):
        return str(self.db_uuid)
    #
    def __str__(self):
        return self.__unicode__()

    class Meta:
        abstract = True
