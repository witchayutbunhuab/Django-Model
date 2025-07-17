from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField()

    def __str__(self):
        return self.text
