
#--------------------------------------Here we import file from another files--------------------------------------------------------
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from views import signup_view,login_view,feed_view, post_view, like_view, comment_view
urlpatterns = [
    #-----------------------------------Create a url for open a views link-----------------------------------------------------------
    url('post/', post_view),
    url('feed/', feed_view),
    url('like/', like_view),
    url('comment/', comment_view),
    url(r'^admin/', admin.site.urls),
    url(r'^signup',signup_view),
    url(r'^login',login_view)

]
