from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from yaml import serialize

from .serializers import BookSerializers
from .models import Book
from  rest_framework import  generics,status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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

    def get(self,request,pk):
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



# class BookDeleteView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

class BookDeleteView(APIView):

        def delete(self,request,pk):
            try:
                book=Book.objects.get(id=pk)
                book.delete()
                return Response(
                    {
                    "status":True,
                    "message":"Successfully delete"

                        },
                        status=status.HTTP_200_OK)
            except Exception:
                return Response(
            {
                "status":False,
                "message":"Book is not found"
                 },
                status=status.HTTP_400_BAD_REQUEST
                     )



# class BookUpdateView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

class BookUpdateView(APIView):
    def put(self,request,pk):
        book=get_object_or_404(Book.objects.all(),id=pk)
        data=request.data
        serializer=BookSerializers(instance=book,data=data,partial=True)
        if serializer.is_valid():
            book_saved=serializer.save()
        return Response(
            {
                "status":True,
                "message":f"Book {book_saved} update successfully "
            }
        )


class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
#
# class BookCreateApiView(APIView):
#     def post(self, request):
#         serializer = BookSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "status": "Books are saved to database",
#                 "data": serializer.data
#             }
#             return Response(data, status=status.HTTP_201_CREATED)
#
#         # ❗️ Agar xato bo‘lsa, bu yerda ham Response qaytadi
#         return Response(
#             {
#                 "status": False,
#                 "message": "Ma'lumotlar noto‘g‘ri!",
#                 "errors": serializer.errors
#             },
#             status=status.HTTP_400_BAD_REQUEST
#         )


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
class BookUpdateDeatailApiView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookViewsSet(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class = BookSerializers




