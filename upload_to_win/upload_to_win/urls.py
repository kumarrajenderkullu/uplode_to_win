
from django.conf.urls import url
from django.contrib import admin

from upload_to_win.upload_to_win.views import home_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home', home_view),

]
