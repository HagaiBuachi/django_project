from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICE = (
    ('A','Action'),
    ('D', 'Drama')
)

class Play(models.Model):
    title = models.CharField(max_length=150)
    plot = models.TextField(max_length=900)
    slug = models.SlugField(unique=True, null=True)
    cast = models.CharField(max_length=500, default=0)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=10)
    image = models.ImageField(upload_to='movie')
    year = models.DateTimeField()
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

RATE_CHOICES = [
    (1, '1 - Trash'),
    (2, '2 - Bad'),
    (3, '3 - OK'),
    (4, '4 - Very Good'),
    (5, '5 - Master Piece'),
]


class Review(models.Model):



    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    movie = models.ForeignKey(Play, blank=True, null=True, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.ManyToManyField(User, related_name='blog_comment')
    class Meta:
        unique_together = ['user','movie']


    def count_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.movie.title} 'User:' {self.user}"


















