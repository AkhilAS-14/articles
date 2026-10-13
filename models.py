from django.db import models
from django.contrib.auth.models import User


class article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    thumb = models.ImageField(
        upload_to='media/',
        null=True,
        blank=True
    )

    author = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.article.price * self.quantity

    def __str__(self):
        return f"{self.user.username} - {self.article.title}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.article.title}"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(
        null=True,
        blank=True
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.title