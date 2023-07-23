from django.db import models

# Create your models here.

CHOICES = (
    ("WD", "Web Development"),
    ("AD", "Android Development"),
    ("DD", "Desktop Development"),
)


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=10000)
    created_at = models.DateTimeField()
    published = models.BooleanField(default=False)
    email = models.EmailField(max_length=254, null=True, blank=True)
    views_count = models.IntegerField(default=0)
    category = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self) -> str:
        return self.title
