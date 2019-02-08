from django.db import models
from datetime import datetime

class Feedback(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=500)
    subject=models.TextField()
    message=models.TextField()
    date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
