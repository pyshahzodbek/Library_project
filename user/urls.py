from django.urls import path

from user.views import CreateApeView,VerifyApiView,NewVerifyApiView

urlpatterns=[
    path('signup/',CreateApeView.as_view()),
    path('verify/',VerifyApiView.as_view()),
    path('new-verify/',NewVerifyApiView.as_view()),

]