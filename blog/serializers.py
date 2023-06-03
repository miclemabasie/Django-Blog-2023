from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from .models import Post, Category, Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    # tags = serializers.SerializerMethodField(source="tags")

    # def get_tags(self, obj):
    #     return obj.tags.names()

    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "author",
            "category",
            "body",
            "publish",
            "image",
            "created",
            "updated",
            "status",
            # "tags",
        ]


class PostSerializer2(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = "__all__"
