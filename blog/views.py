from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from base.service import generate_order_book
from .filter import CategoryBlogFilter
from .models import Blog, Review, Commentary, Category
from .serializers import CreateBlogSerializer, DetailListBlogSerializer, \
    CommentSerializer, RateSerializer, \
    BlogSerializer, ListCommentSerializer, CategoryListSerializer, \
    CategorySerializer, RecentBlogSerializer
from rest_framework import generics


class CreateBlogView(generics.CreateAPIView):
    serializer_class = CreateBlogSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UpdateBlogView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CreateBlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        query = Blog.objects.filter(pk=pk)
        query.delete()
        return Response({"detail": "блог успешно удален"})

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class RetrieveListBlogView(generics.RetrieveAPIView):
    serializer_class = DetailListBlogSerializer
    queryset = Blog.objects.all()
    lookup_field = 'pk'


class ListBlogView(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CategoryBlogFilter



class CreateCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        blog = self.kwargs['blog_id']
        serializer.save(blog_id=blog)

    def get_queryset(self):
        return Commentary.objects.filter(
            blog_id=self.kwargs['blog_id']
        )


class DeleteCommentView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Commentary.objects.all()

    def delete(self, request, *args, **kwargs):
        query = Commentary.objects.filter(
            blog_id=self.kwargs['blog_id'],
            pk=self.kwargs['pk']
        )
        query.delete()
        return Response({"detail": "Комантрия удален"})

    def get_queryset(self):
        return Commentary.objects.filter(
            blog_id=self.kwargs['blog_id'],
            pk=self.kwargs['pk']
        )


class ListCommentView(generics.ListAPIView):
    serializer_class = ListCommentSerializer
    queryset = Commentary.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            blog_id=self.kwargs['blog_id']
        )


class ListCategoryView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CreateRateView(generics.CreateAPIView):
    serializer_class = RateSerializer
    queryset = Review.objects.all()


    def perform_create(self, serializer):
        blog = self.kwargs['blog_id']
        user = self.request.user
        serializer.save(author=user, blog_id=blog)

    def get_queryset(self):
        return self.queryset.filter(
            blog_id=self.kwargs['blog_id']
        )


#
class RecentBLogView(generics.ListAPIView):
    serializer_class = RecentBlogSerializer
    queryset = Blog.objects.all()

    def get_queryset(self):
        query = Blog.objects.filter(
            category__category_blog__id__in=[self.kwargs['blog_id']]
        ).distinct().exclude(pk=self.kwargs['blog_id'])
        return query[:3]

class IndexRecentBLogView(generics.ListAPIView):
    serializer_class = RecentBlogSerializer
    queryset = Blog.objects.order_by('-id')[:5]
