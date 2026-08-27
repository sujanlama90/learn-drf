from rest_framework import serializers
from .models import Blog , Comment

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
       model = Comment
       fields = '__all__'


class BlogSerializers(serializers.ModelSerializer):
    comments  = CommentSerializers(many = True,read_only = True) #write variable name from related_name of model
    class Meta:
        model = Blog
        fields = '__all__'