from rest_framework import serializers
from ...models import Comment
from blog.models import Post


class CommentListSerializer(serializers.ModelSerializer):

    snippet = serializers.ReadOnlyField(source="get_snippet")
    user = serializers.CharField(read_only=True)
    post = serializers.SlugRelatedField(slug_field="title", queryset=Post.objects.all())
    content = serializers.CharField(write_only=True)
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["user", "post", "snippet", 'content',"absolute_url", "created_at"]

    def get_absolute_url(self, obj):

        request = self.context.get("request")
        return request.build_absolute_uri(obj.get_absolute_url())

    def create(self, validated_data):

        request = self.context.get("request")
        validated_data["user"] = request.user.profile
        return super().create(validated_data)

class CommentDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    post = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Comment
        fields = ["user", "post", "content", "created_at"]