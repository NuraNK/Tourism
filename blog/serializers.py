from accounts.models import User
from .models import Commentary, Blog, ReviewTotal, Review, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
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
    user = UserSerializer(read_only=True)
    reviews = serializers.SerializerMethodField()
    count_comment = serializers.SerializerMethodField()
    comment = CommentSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Blog
        fields = (
            'id',
            'category',
            'user',
            'title',
            'image',
            'description',
            'created',
            'modified',
            'reviews',
            'count_comment',
            'comment',
        )

    def get_count_comment(self, obj):
        count = (obj.comment.all().count())
        return count

    def get_reviews(self, obj):
        return ReviewTotalSerializer(obj.blog_totals.all().first()).data


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    count_comment = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = (
            'id',
            'category',
            'title',
            'modified',
            'count_comment',
        )
    def get_count_comment(self, obj):
        count = (obj.comment.all().count())
        return count

