from datetime import datetime

from django.shortcuts import render
from rest_framework.exceptions import ValidationError

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from shared.unitily import send_email
from user.models import User, NEW, CODE_VERIFIED
from user.serializers import SignUpSerializer


# Create your views here.
class CreateApeView(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=SignUpSerializer
    permission_classes = (permissions.AllowAny,)

class VerifyApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request,*args,**kwargs):
        user=request.user
        code=request.data.get('code')
        print(user)
        print(code)
        self.check_verify(user,code)
        return Response(
            {
                'success':True,
                "auth_status":user.auth_status,
                "access":user.token()['access'],
                "refresh_token":user.token()["refresh_token"]


            }

        )
    @staticmethod
    def check_verify(user,code):
        verifies=user.verify_code.filter(code=code,expiration_time__gte=datetime.now(),is_confirmed=False)
        if not verifies.exists():
            raise ValidationError(
                {
                    "message":"Kiritilgan kod yaroqsiz!"
                }
            )
        else:
            verifies.update(is_confirmed=True)
        if user.auth_status==NEW:
            user.auth_status=CODE_VERIFIED
            user.save()
        return True
class NewVerifyApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self,request,*args,**kwargs):
        user=request.user
        self.check_verify(user)
        if user.email:
            code=user.create_verify_code()
            send_email(user.email,code)
        else:
            raise ValidationError(
                {
                    "message":"Email manzilni kiriting!"
                }
            )

        return Response(
            {
                "message":"Kod muvafaqiyatli qayta yuborildi!"
            }
        )
    @staticmethod
    def check_verify(user):
        verifies=user.verify_code.filter(expiration_time__gte=datetime.now(),is_confirmed=False)
        if verifies.exists():
            raise ValidationError(
                {
                    "message":"Sizning tasdiqlash kodingiz hali yaroqli!"
                }
            )