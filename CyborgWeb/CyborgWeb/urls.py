from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('discover/', views.discover, name='discover'),
    path('news/', views.news, name='news'),
    # path('indie/', views.indie, name='indie'),
    path('profile/', views.profile, name='profile'),
    path('game/', include('game.urls')),
    path('comment/', views.comment, name='comment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)