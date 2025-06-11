from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from  .models import Book

class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model=Book
        fields=('id','title','subtitle','context','author','isbn','price')



    def validate(self,data):
        title=data.get("title",None)
        author=data.get("author",None)
        if not title.isalpha():
            raise ValidationError(
                {
                    "status":False,
                    "message":"Kitob sarlavhasi harflardan iborat bulishi kerak!"
                }
            )

        if Book.objects.filter(author=author,title=title).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi bilan muallif bir martadan kiritish kerak!"
                }
            )
        return  data

    def validated_price(self,price):
        if price<0 or price>999999999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob narxini tug'ri kiriting!"
                }
            )
