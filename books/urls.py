from django.urls import path
from .views import BookListView,BookDetailView,BookUpdateView,BookDeleteView

urlpatterns=[
    path('',BookListView.as_view(),),
    path('<int:pk>/',BookDetailView.as_view()),
    path('<int:pk>/update/',BookUpdateView.as_view()),
    path('<int:pk>/delete/',BookDeleteView.as_view())

]