from django.urls import path, include
from . import views
import posts.views as post_views
import comments.views as comment_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'), 
    path('posts', post_views.uploadpost, name='posts'),
    path('delete_post', post_views.deletepost, name='delete_post'),
    path('chat/', include('chat.urls'))
]