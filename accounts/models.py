from django.db import models
from django.conf import settings

from posts.models import PostKey

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_keys = models.ManyToManyField(PostKey)
    # following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')
    # verification_code = models.CharField(max_length=64)
    # is_verified = models.BooleanField(default=False)
    # password_reset_active = models.BooleanField(default=False)
    # password_reset_key = models.CharField(max_length=64, blank=True, null=True)

    def __unicode__(self):
        if self.user.first_name and self.user.last_name:
            return "%s %s" % (self.user.first_name, self.user.last_name)
        return self.user.email

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return "%s %s" % (self.user.first_name, self.user.last_name)
        return self.user.email

    # def get_absolute_url(self):
    #     return reverse('accounts:user_detail', kwargs= {'pk': self.user.id})
