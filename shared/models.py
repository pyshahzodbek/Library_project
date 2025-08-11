import uuid

from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id=models.UUIDField(unique=True,default=uuid.uuid4 ,editable=False,primary_key=True)
    created_time=models.TimeField(auto_now_add=True)
    update_time=models.TimeField(auto_now=True)

    class Meta:
        abstract=True