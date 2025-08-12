import random
import uuid
from datetime import timedelta
from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

from shared.models import BaseModel
from django.db import models

# Create your models here.
MANAGER,ADMIN,REGULAR=("manager",'admin','regular')
NEW,CODE_VERIFIED,DONE=("new",'code_verified','done')

class User(AbstractUser,BaseModel):
    USER_ROLES=(
        (MANAGER,MANAGER),
        (ADMIN,ADMIN),
        (REGULAR,REGULAR)
    )
    AUTH_STATUS=(
        (NEW,NEW),
        (CODE_VERIFIED,CODE_VERIFIED),
        (DONE,DONE)
    )



    user_role=models.CharField(max_length=31,choices=USER_ROLES,default=REGULAR)
    auth_status=models.CharField(max_length=31,choices=AUTH_STATUS,default=NEW)
    email=models.EmailField(max_length=31,unique=True,)

    def __str__(self):
       return  self.username

    @property
    def full_name(self):
        return self.username
    def create_verify_code(self):
        code="".join([str(random.randint(0,9))for _ in range(4)])
        UserConfirmation.objects.create(
            user_id=self.id,
            email=self.email,
            code=code
        )
        return code

    def check_username(self):
        if not self.username:
            temp_username = f'library-{uuid.uuid4().__str__().split("-")[-1]}'  # instagram-23324fsdf
            while User.objects.filter(username=temp_username):
                temp_username = f"{temp_username}{random.randint(0, 1000)}"
            self.username = temp_username
    def check_email(self):
        if self.email:
            normalize_email=self.email.lower()
            self.email=normalize_email
    def check_pass(self):
        if not self.password:
            temp_password=f"password-{uuid.uuid4().__str__().split("-")[-1]}"
            self.password=temp_password
    def hashing_password(self):
        if not self.password.startswith("pbkdf2_sha256"):
            self.set_password(self.password)
    def token(self):
        refresh=RefreshToken.for_user(self)
        return {
            "access":str(refresh.access_token),
            "refresh_token":str(refresh)
        }
    def clean(self):
        self.check_username()
        self.check_email()
        self.check_pass()
        self.hashing_password()
    def save(self,*args,**kwargs):
        self.clean()
        super(User,self).save(*args,**kwargs)



EMAIL_EXPRE=5

class UserConfirmation(BaseModel):

    id=models.UUIDField(unique=True,default=uuid.uuid4,editable=False,primary_key=True)
    email=models.EmailField(max_length=31,unique=True)
    code=models.CharField(max_length=4,)
    user=models.ForeignKey("user.User",models.CASCADE,related_name="verify_code")
    expiration_time=models.DateTimeField(null=True)
    is_confirmed=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.__str__())

    def save(self,*args,**kwargs):
        if self.email:
            self.expiration_time=datetime.now()+timedelta(minutes=EMAIL_EXPRE)
        super().save(*args,**kwargs)




