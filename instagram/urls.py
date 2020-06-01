from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.main, name='main_page'),
    path(r'new/post', views.new_post, name='new-post'),
    path(r'update_post/(<int:pk>)/', views.update_post, name='updatepost'),
    path(r'delete_post/(<int:pk>)/', views.delete_post, name='deletepost'),
    path(r'profile/', views.profile, name = 'profile'),
    path(r'(<int:image_id>)/', views.single_post, name = 'single_image'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)