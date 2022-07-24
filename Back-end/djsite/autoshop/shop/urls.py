from django.urls import path, re_path

from .views import *
urlpatterns = [
    path('', AutoHome.as_view(), name='home'),
    path('filter/', FilterAutoView.as_view(), name='filter'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('new/', , name='autonew'),
    # path('by/', autoby, name='autoby'),
]