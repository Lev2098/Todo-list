from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return f"/tags"

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datatime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='tasks')

    class Meta:
        ordering = ["is_done", "-datatime"]

    def get_absolute_url(self):
        return f"/tasks"

    def __str__(self):
        return self.content