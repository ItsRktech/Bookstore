from django.urls import path
from .views import RegisterUserView, LoginView, BookView

urlpatterns = [
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/books/', BookView.as_view(), name='book_list_create'),
    path('api/books/<int:pk>/', BookView.as_view(), name='book_detail_update_delete'),
]