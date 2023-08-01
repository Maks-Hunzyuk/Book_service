
from rest_framework import serializers
from .models import Author, Book



class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'books')

    def to_representation(self, instance): 
        data = super().to_representation(instance)
        if instance.books is None:
            return {}
        else:
            books = []
            for book in instance.books.all():
                books.append(book.title)
            return {'first_name': instance.first_name, 'last_name': instance.last_name,'books': books}
        

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'year_published', 'author')







