from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400)

    def __str__(self) -> str:
        return self.title

class Question(models.Model):
    question = models.CharField(max_length=400)
    pub_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=400)
    pub_date = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(
        Question,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.answer
