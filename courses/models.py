from django.db import models


# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=50)
    course_order = models.IntegerField()
    course_active = models.BooleanField(default=True)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='course_images')

    def __str__(self):
        return self.name  # use for showing names

    class Meta:
        ordering = ['name']  # use for ascending order


class Teachers(models.Model):
    name = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='teacher_images')
    dept = models.CharField(max_length=50)
    teacher_order = models.IntegerField(null=True, blank=True)
    teacher_active = models.BooleanField(null=True, blank=True, default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class PeopleSay(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='people_images')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class LatestArticles(models.Model):
    article_image = models.ImageField(upload_to='articles_images')
    date = models.DateField()
    article_title = models.CharField(max_length=50)
    article_desc = models.TextField()

    def __str__(self):
        return self.article_title

    class Meta:
        ordering = ['article_title']


class ContactUs(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    msg = models.TextField()

    def __str__(self):
        return self.f_name  # use for showing names

    class Meta:
        ordering = ['f_name']  # use for ascending order


class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    heading = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.title  # use for showing names

    class Meta:
        ordering = ['title']  # use for ascending order

