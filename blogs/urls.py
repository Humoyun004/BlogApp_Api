from django.urls import path

from . import views

urlpatterns = [
    path('api/blogs/', views.BlogList.as_view()),
    path('api/new/', views.BlogCreate.as_view()),
    path('api/user/<str:username>/', views.UserPostsList.as_view()),
    path('api/blogs/<int:pk>/', views.BlogRetrieveUpdateDestroy.as_view()),
]