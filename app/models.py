from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField()
    location = models.OneToOneField('Location', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField('Skills', null=True)
    slug = models.SlugField(max_length=100, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Location(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)


class Skills(models.Model):
    name = models.CharField(max_length=50)

