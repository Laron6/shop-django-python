from django.urls import path
from . import views

urlpatterns = [
    path('warpeace/', views.book_detail, name='book_detail'),  # маршрут для отображения книги
]