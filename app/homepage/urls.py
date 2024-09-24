from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name= 'homepage'
urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.news_list, name='news_list'),
    path('news/<int:pk>', views.news_detail, name='news_detail'),
    path('contact', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)