# -*- coding: utf-8 -*-

# Standard library.
from django import template

# Local
from ..version import get_git_revision_string

register = template.Library()

@register.simple_tag
def gitversion():
    if not gitversion.version:
        gitversion.version = get_git_revision_string()
    return gitversion.version
gitversion.version = None
