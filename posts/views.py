from django.db.models import Q
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from rest_framework.permissions import (
    IsAuthenticated,
)

from posts.serializers import (
    PostListSerializer,
)

from posts.models import (
    Post
)

class PostListAPIView(ListAPIView):
    """
    List all the posts
    """
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]
    #pagination_class = PostPageNumberPagination #TODO -> Add this later

    def get_queryset(self, *args, **kwargs):
        queryset = Post.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(content__icontains=query)
            ).distinct()

        return queryset
