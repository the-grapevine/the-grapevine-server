from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)

from posts.models import Post


# TODO --> Need to build the detail view for this
# post_detail_url = HyperlinkedIdentityField(
#     view_name='posts:post-detail',
#     lookup_field='post_key'
# )


class PostListSerializer(ModelSerializer):
    # detail_url = post_detail_url
    post_key = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            # 'detail_url',
            'content',
            'post_key',
            # 'images', # TODO -> Figure out how to add image support
        ]

    def get_post_key(self, obj):
        post_key = obj.post_key.key
        return post_key
