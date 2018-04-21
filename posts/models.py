from django.conf import settings
from django.db import models


class PostKey(models.Model):
    """
    A key that the user has added to their profile so that they can
    get points for each post that they make
    """
    key = models.CharField(max_length=120)

    def __unicode__(self):
        return self.key

    def __str__(self):
        return self.key


class ImageUpload(models.Model):
    """
    A post can have multiple images so post has a many to many relationship
    with ImageUpload
    """
    def get_upload_location(instance, filename):
        return 'uploads/potsts/%s' % filename

    image = models.ImageField(upload_to=get_upload_location,
                                null=True,
                                blank=True,
                                width_field="image_width_field",
                                height_field="image_height_field",
                            )
    image_width_field = models.IntegerField(default=0)
    image_height_field = models.IntegerField(default=0)


class Post(models.Model):
    """
    Creates a post
    """
    # Allows the user to attain points without revealing identity.
    # Post keys are added to the user profile
    post_key = models.OneToOneField(PostKey, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    images = models.ManyToManyField(ImageUpload, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.post_key.key

    def __str__(self):
        return self.post_key.key
