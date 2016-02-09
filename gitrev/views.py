# -*- coding: utf-8 -*-

from rest_framework import views
from rest_framework.response import Response


class RevisionView(views.APIView):
    http_method_names = ['get', ]

    def get(self, request):
        data = {}
        context = self.get_context_data(self.kwargs)
        print('>>>>>>>>>>>>>>>', context['appversion'])
        appversion = getattr(request, 'appversion', None)
        if appversion:
            data['version'] = appversion
        return Response(data)
