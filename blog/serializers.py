from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .models import Post, Category, Comment
from rest_framework import serializers


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    url = serializers.SerializerMethodField()
    intro = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    author_img = serializers.SerializerMethodField()

    def get_url(self, obj):
        return obj.get_absolute_url()

    def get_intro(self, obj):
        return obj.get_intro()

    def get_author(self, obj):
        if obj.author.username:
            return obj.author.username
        else:
            return obj.author.email

    def get_author_img(self, obj):
        return obj.get_author_image()

    class Meta:
        model = Post
        fields = "__all__"
