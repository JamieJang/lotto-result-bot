from django.conf.urls import url
from django.contrib import admin

from lottoresult.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^keyboard/',keyboard),
    url(r'message',answer),
]
