from django.contrib import admin

from posts import models

posts_models = [
    models.Post,
    models.PostKey,
    models.ImageUpload
]

admin.site.register(posts_models)
