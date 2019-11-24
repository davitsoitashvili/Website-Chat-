from django.db import models

class Message(models.Model):
    author = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.message