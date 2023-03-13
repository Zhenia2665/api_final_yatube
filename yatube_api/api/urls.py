from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()

v1_router.register(r"^posts", PostViewSet, basename="post")
v1_router.register(r"^groups", GroupViewSet, basename="group")
v1_router.register(
    r"^posts/(?P<post_id>\d+)/comments",
    CommentViewSet,
    basename="comment")

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path("v1/follow/", FollowViewSet.as_view()),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
