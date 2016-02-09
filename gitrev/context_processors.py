# -*- coding: utf-8 -*-
from . import __version__


def appversion(request):
    """Stuff the __version__ into RequestContext."""
    return {'appversion': __version__}
