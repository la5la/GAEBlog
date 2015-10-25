#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '连天'
__email__ = "liantian@188.com"


# Stdlib imports

# Core Django imports
# from django.contrib.auth.models import User
# Third-party app imports

# Imports from your apps
class User:
    is_superuser = True
    is_active = True
    is_staff = True
    id = 1
    pk = 1


def return_true(*args, **kwargs):
    return True


User.has_module_perms = return_true
User.has_perm = return_true


class Middleware(object):
    def process_request(self, request):
        request.user = User()
