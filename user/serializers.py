from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User,UserConfirmation
from shared.unitily import check_email, send_email


class SignUpSerializer(serializers.ModelSerializer):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['user_email']=serializers.CharField(required=False)

    class Meta:
        model=User
        fields=[
            "id",
            'auth_status',
        ]
        extra_kwargs={
            'user_status':{"read_only":True,"required":False},
        }
    def create(self, validated_data):
        user=super().create(validated_data)
        if user.email:
           code= user.create_verify_code()
           send_email(user.email,code)
        user.save()
        return user

    def validate(self,attrs):
        data=super().validate(attrs)
        data=self.auth_validate(data)
        return data
    @staticmethod
    def auth_validate(data):
        user_input=str(data.get('user_email')).lower()
        input_type=check_email(user_input)
        if input_type=='email':
            data={
                "email":user_input,
            }
        else:
            data={
                "success":False,
                 "message":"Invalid email"
            }
            raise ValidationError(data)
        return data
    def validate_user_email(self,value):
        value=value.lower()
        if value and User.objects.filter(email=value).exists():
            raise ValidationError(
                {
                    "success":False,
                    "message":"Email already exists!"
                }
            )
        return value
    def to_representation(self, instance):
        data=super().to_representation(instance)
        data.update(instance.token())
        return data




