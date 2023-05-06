from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name = 'home'),
    path('<slug':slug>/' viees.PostDetsil.as_view(), name='post_detail'),
]