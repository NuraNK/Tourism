from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Avg
from .models import Rating, Reviews, Blog, RatingResult
from .serializers import RatingSerializer, ReviewsSerializer, BlogSerializer, RatingUpdateSerializer, RatingResultSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, \
    DestroyAPIView

from .serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import parser_classes
from collections import Counter

@parser_classes([MultiPartParser, FormParser])
class ImageUploadView(CreateAPIView):
    serializer_class = ImageSerializer
    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file') # забираем список файлов из запроса
        results = []
        for file in files:
            file_dict = {}
            file_dict['file'] = file # переводим файл из запроса в словарь для сериализатора
            file_serializer = ImageSerializer(data=file_dict)
            if file_serializer.is_valid(raise_exception=True):
                file_serializer.save()
                results.append(file_serializer.data) # добавляем в список с результатами
        return Response(results, status=status.HTTP_201_CREATED)

class BlogCreateView(CreateAPIView):
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class BlogListView(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def get(self, request, *args, **kwargs):
        rating = Rating.objects.filter(
            blog_id=self.kwargs['blog_id']
        )
        sum = 0
        for rate in rating:
            sum += (int(str(rate.star)))
        if sum > 0:
            sum = round(sum/len(rating))
        Blog.objects.update(
            rating_result=sum
        )
        return self.list(self,request)

    def get_queryset(self):
        return self.queryset.filter(
            pk=self.kwargs['blog_id']
        )

class BlogUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        blog = self.queryset.filter(pk=pk)
        blog.delete()
        return Response({"result": "Блог успешно удалено"})


class RatingCreateView(APIView):

    def post(self, request, *args, **kwargs):
        user = self.request.user
        blog = self.request.data.get('blog')
        star = self.request.data.get('star')
        query = Rating.objects.filter(
            user=user
        )
        if query:
            query.delete()
        try:
            Rating.objects.create(
                user=user,
                blog_id=blog,
                star_id=star
            )


        except IntegrityError:
            return Response({"detail":"Неверное значение"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail":"Рейтинг успешно поставлен"},status=status.HTTP_200_OK)

class RatingUpdateView(UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingUpdateSerializer
    lookup_field = 'blog_id'
    def get_queryset(self):
        user = self.request.user
        print(self.kwargs['blog_id'])
        return self.queryset.filter(
            user=user, blog_id=self.kwargs['blog_id']
        )

class RatingDestroyView(DestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingUpdateSerializer
    lookup_field = 'blog_id'

    def get_queryset(self):
        user = self.request.user
        print(self.kwargs['blog_id'])
        return self.queryset.filter(
            user=user, blog_id=self.kwargs['blog_id']
        )


class RatingListView(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    lookup_field = 'blog_id'

    def get_queryset(self):
        return self.queryset.filter(
            blog_id=self.kwargs['blog_id']
        )


class ReviewView(CreateAPIView):
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class ReviewListView(ListAPIView):
    serializer_class = ReviewsSerializer
    queryset = Reviews.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            blog_id=self.kwargs['blog_id']
        )

