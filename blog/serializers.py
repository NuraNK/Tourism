from accounts.models import User
from .models import Rating, Reviews, Blog, RatingResult, Image
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
        )

class BlogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = (
            'id',
            'user',
            'title',
            'image',
            'description',
            'rating_result',

        )

class RatingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingResult
        fields = (
            'id',
            'blog',
            'rating',
        )
class RatingSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    # blog = BlogSerializer(read_only=True)
    class Meta:
        model = Rating
        fields = (
            'id',
            # 'user',
            'star',
            'blog',
        )

class RatingUpdateSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    # blog = BlogSerializer(read_only=True)
    class Meta:
        model = Rating
        fields = (
            'id',
            # 'user'
            'star',
            # 'blog'
        )

class ReviewsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Reviews
        fields = (
            'id',
            'user',
            'text',
            'blog'
        )


