"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
#from django.conf.urls import url
#from django.contrib import admin


#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#]


from django.conf.urls import patterns, include, url
#from django.contrib import admin

#admin.autodiscover()

#urlpatterns = patterns('',
    #Examples

 #   url(r'^admin', include(admin.site.urls)),
 #   url(r'^myapp/', include('myapp.url')),
#)


from rest_framework_nested import routers

from authentication.views import AccountViewSet, IndexView


router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)


urlpatterns = patterns(
     '',
    # ... URLs
    url(r'^api/v1/', include(router.urls)),

    url('^.*$', IndexView.as_view(), name='index'),
)