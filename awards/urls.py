
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from appawards import views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token



app_name='ratings'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('appawards.urls')),
    url(r'^accounts/logout/', auth_views.LogoutView, {'next_page': '/'}, name='logout'),
    url( r'^login/$',auth_views.LoginView.as_view(template_name="useraccounts/login.html"), name="login"),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^search/$', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)