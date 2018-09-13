"""bus_agency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView, RedirectView
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _('Bus agency')
admin.site.site_title = _('Bus agency admin')
admin.site.index_title = _('Bus agency admin')

urlpatterns = [
    # url(r'^control/', include('apps.control.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include('apps.control.urls')),
    # url(r'^$', TemplateView.as_view(template_name='layouts/default.html')),
    url(r'^$', RedirectView.as_view(url='/admin', permanent=False))
]
