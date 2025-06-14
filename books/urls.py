from django.urls import path
from .views import BookListView,BookDetailView,BookUpdateView,BookDeleteView,\
    BookCreateApiView,BookUpdateDeatailApiView,BookUpdateDeleteView,BookViewsSet
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register('books',BookViewsSet,basename='books')

urlpatterns=[
    # path('',BookListView.as_view()),
    # path('book/create/',BookCreateApiView.as_view()),
    # path('book/<int:pk>/',BookUpdateDeatailApiView.as_view()),
    # path('book/update/delete/<int:pk>/',BookUpdateDeleteView.as_view()),
    # path('<int:pk>/',BookDetailView.as_view()),
    # path('<int:pk>/update/',BookUpdateView.as_view()),
    # path('<int:pk>/delete/',BookDeleteView.as_view())

]
urlpatterns=urlpatterns+router.urls