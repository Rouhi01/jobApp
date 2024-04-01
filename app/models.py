from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.name


TypeChoices = (
    ('Full time', 'Full time'),
    ('Part time', 'Part time')
)


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField()
    type = models.CharField(max_length=10, choices=TypeChoices)
    location = models.OneToOneField('Location', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    skills = models.ManyToManyField('Skills')
    slug = models.SlugField(max_length=100, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(null=True, blank=True)

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

    def __str__(self):
        return f'{self.city}-{self.country}'


class Skills(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

