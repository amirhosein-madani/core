from rest_framework import serializers
from ...models import Post, Category

# class PostSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     author = serializers.CharField()
#     title = serializers.CharField(max_length = 255)
#     created_at = serializers.DateTimeField()
#     status = serializers.BooleanField()


class CategorySerializer(serializers.ModelSerializer):
    """
    this is a serializer for CategoryModel
    """

    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "absolute_url", "is_active"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.get_absolute_url())


class PostSerializer(serializers.ModelSerializer):
    """
    this is a serializer for PostModel
    """

    published_date = serializers.DateTimeField()
    snippet = serializers.ReadOnlyField(source="get_snippet")
    absolute_url = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Category.objects.all()
    )
    # category = CategorySerializer(many = True , read_only= True )
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "content",
            "snippet",
            "absolute_url",
            "category",
            "created_at",
            "published_date",
            "status",
        ]

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

        data["category"] = CategorySerializer(
            instance.category.all(), many=True, context=self.context
        ).data

        return data

    def create(self, validated_data):

        request = self.context.get("request")
        validated_data["author"] = request.user.profile
        return super().create(validated_data)
