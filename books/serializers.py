from rest_framework import serializers
from  .models import Book

class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model=Book
        fields=('id','title','subtitle','context','author','isbn','price')

