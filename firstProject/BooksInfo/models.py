from django.db import models

# Create your models here.

class Book(models.Model):
    Bookid=models.IntegerField()
    BookName=models.TextField()
    Author=models.TextField()
    Publication=models.TextField()
    CreateAt=models.DateField()
    UpdateAt=models.DateField()

    def __str__(self) :
        return self.BookName
