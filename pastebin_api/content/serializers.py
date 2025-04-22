from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Content

class ContentSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username', read_only=True)
    class Meta:
        model = Content
        fields = "__all__"
        extra_kwargs = {
            'token': {'read_only': True},
            'owner': {'read_only': True},
            'created': {'read_only': True},
            'last_edit': {'read_only': True},
        }

    # def validate(self, attrs):
    #     if self.instance:
    #         if not attrs.get('title') and not attrs.get('content'):
    #             raise serializers.ValidationError("Either 'title' or 'content' must be provided.")
    #     else:
    #         if not attrs.get('title') or not attrs.get('content'):
    #             raise serializers.ValidationError("Either 'title' or 'content' must be provided.")
    #
    #     if 'title' in attrs and attrs['title'].strip() == '':
    #         raise serializers.ValidationError("'title' cannot be blank.")
    #
    #     if 'content' in attrs and attrs['content'].strip() == '':
    #         raise serializers.ValidationError("'content' cannot be blank.")
    #
    #     return attrs

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
