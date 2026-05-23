from rest_framework import serializers
from ...models import Comment
from blog.models import Post


class CommentSerializer(serializers.ModelSerializer):

    snippet = serializers.ReadOnlyField(source="get_snippet")
    user = serializers.CharField(read_only=True)
    post = serializers.SlugRelatedField(slug_field="title", queryset=Post.objects.all())

    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["user", "post", "snippet", "content", "absolute_url", "created_at"]

    def get_absolute_url(self, obj):

        request = self.context.get("request")
        return request.build_absolute_uri(obj.get_absolute_url())

    def to_representation(self, instance):
        """
        this is a function for overwrite fields to show
        """

        request = self.context.get("request")
        data = super().to_representation(instance)

        if request.parser_context.get("kwargs").get("pk"):

            data.pop("snippet", None)
            data.pop("absolute_url", None)
        else:

            data.pop("content", None)

        return data

    def create(self, validated_data):

        request = self.context.get("request")
        validated_data["user"] = request.user.profile
        return super().create(validated_data)
