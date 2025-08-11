from django.urls import path

from user.views import CreateApeView

urlpatterns=[
    path('signup/',CreateApeView.as_view()),


]