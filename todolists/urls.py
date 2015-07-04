"""todolists URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
# from django.contrib import admin
# flows goes from | test.py->look for in url.py->look for view of url in
# view.py
urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # if we comment out following our test will give us resolver404 error
    # ^$ is root's url, send requests to home_page view
    url(r'^$', 'lists.views.home_page', name='home')
]
