from django.shortcuts import render
from rest_framework.views import APIView
from yaml import serialize

from .serializers import BookSerializers
from .models import Book
from  rest_framework import  generics,status
from rest_framework.response import Response

# class BookListView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

class BookListView(APIView):

    def get(self,request):
        books=Book.objects.all()
        serializer_date=BookSerializers(books,many=True)
        date={
            "status":f"Returned {len(books)} books ",
            "books":serializer_date.data
        }
        return  Response(date)

# class BookDetailView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers


class BookDetailView(APIView):

    def get(self,requset,pk):
        try:
            book=Book.objects.get(id=pk)
            serializer=BookSerializers(book).data
            date={
                "Status":"Successful",
                "book":serializer
                }
            return  Response(date)
        except Exception:
            return Response(
                {
                    "status":'Does not exits',
                    "message":" Book is nod found"
                } ,status=status.HTTP_404_NOT_FOUND
            )



class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

class BookCreateApiView(APIView):
    def post(self,request):
       date=request.date
       serializer=BookSerializers(date=date)
       if serializer.is_valid():
            serializer.save()
            date={
                "status":"Books are saved to datebase",
                "date":date
            }
            return Response(date)

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
class BookUpdateDeatailApiView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers



