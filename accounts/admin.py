from django.contrib import admin

from accounts import models

accounts_models = [
    models.UserProfile
]

admin.site.register(accounts_models)
