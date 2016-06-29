from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import generic
from main.models import *
from datetime import datetime


class IndexView(TemplateView):
    template_name = 'main.html'

    def get(self, request):

        posts = Post.objects.filter(publish=True)

        return self.render_to_response({
            'title': 'coffe and cake',
            'posts': posts,
        })


# last_modified_date = timezone.now()
# @last_modified(lambda req, **kw: last_modified_date)
# def cached_javascript_catalog(request, domain='djangojs', packages=None):
#     """ Закэшированный каталог JS-перевода """
#     if packages is None:
#         app_configs = apps.get_app_configs()
#         packages = set(app_config.name for app_config in app_configs)
#
#     packages.add('django.conf')
#     return javascript_catalog(request, domain, packages)