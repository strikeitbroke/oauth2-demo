from django.db import models


class Todo(models.Model):
    entry = models.TextField()
