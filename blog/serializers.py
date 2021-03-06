from accounts.models import User
from accounts.serializers import ProfileInfoSerializer
from .models import Commentary, Blog, ReviewTotal, Review, Category, Tag
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name'
        )

class CategoryListSerializer(serializers.ModelSerializer):
    category_blog = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'category_blog'
        )

    def get_category_blog(self, obj):
        return obj.category_blog.all().count()


class ReviewTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewTotal
        fields = ('rate', 'total')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
        )


class CreateBlogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = (
            'id',
            'category',
            'user',
            'title',
            # 'paragraph',
            # 'tag',
            # 'description',
            'image',
            'description',

        )


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'rate',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'created',
            'text',
        )


class ListCommentSerializer(serializers.ModelSerializer):
    count_comment = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Commentary
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'text',
            'count_comment'
        )


class DetailListBlogSerializer(serializers.ModelSerializer):
    user = ProfileInfoSerializer(read_only=True)
    reviews = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    count_comment = serializers.SerializerMethodField()
    comment = CommentSerializer(many=True)
    category = CategorySerializer(many=True)
    tag = TagSerializer(many=True)

    class Meta:
        model = Blog
        fields = "__all__"

    def get_count_comment(self, obj):
        count = (obj.comment.all().count())
        return count

    def get_description(self, obj):
        desc = obj.description.html
        return desc

    def get_reviews(self, obj):
        return ReviewTotalSerializer(obj.blog_totals.all().first()).data


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    user = ProfileInfoSerializer()
    count_comment = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'id',
            'category',
            'title',
            'image',
            'created',
            'user',
            'count_comment',
        )

    def get_count_comment(self, obj):
        count = (obj.comment.all().count())
        return count

class RecentBlogSerializer(serializers.ModelSerializer):
    user = ProfileInfoSerializer()
    count_comment = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'id',
            # 'category',
            'title',
            'image',
            'created',
            'user',
            'count_comment',
        )

    def get_count_comment(self, obj):
        count = (obj.comment.all().count())
        return count
