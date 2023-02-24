from rest_framework import serializers
from BooksInfo.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['Bookid','BookName','Author','Publication','CreateAt','UpdateAt']
        