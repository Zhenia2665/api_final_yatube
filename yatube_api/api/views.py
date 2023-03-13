from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)

from posts.models import Group, Post, User


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('group',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для обработки групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки комментариев."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """Вьюсет для обработки подписок."""
    serializer_class = FollowSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('user__username', 'following__username')
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # new_queryset = Follow.objects.filter(user=self.request.user)
        # return new_queryset
        user = self.request.user
        queryset = user.follower.all()
        follower = self.request.query_params.get('search', None)

        if follower is not None:
            user_2 = User.objects.get(username=follower)
            queryset = queryset.filter(following=user_2)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get(self, request, *args, **kwargs):
    #     user = self.request.user
    #     queryset = user.follower.all()
    #     follower = self.request.query_params.get('search', None)
    #     print(follower)
    #     if follower is not None:
    #         user_2 = User.objects.get(username=follower)
    #         queryset = queryset.filter(following=user_2)

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
