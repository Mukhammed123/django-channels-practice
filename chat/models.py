from django.db import models


class Message(models.Model):
    message = models.CharField(max_length=2500)
    author = models.CharField(max_length=100)

    def __str__(self):
        return {
            'message': self.message,
            'author': self.author
        }
