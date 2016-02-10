# -*- coding: utf-8 -*-

from rest_framework import views
from rest_framework.response import Response

from . import __version__


class RevisionView(views.APIView):
    http_method_names = ['get', ]

    def get(self, request):
        data = {}
        if appversion:
            data['version'] = __version__
        return Response(data)
