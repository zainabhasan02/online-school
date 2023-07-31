from django.contrib import admin

from .models import Courses, Teachers, PeopleSay, LatestArticles, ContactUs, AboutUs

# Register your models here.
admin.site.register(Courses)
admin.site.register(Teachers)
admin.site.register(PeopleSay)
admin.site.register(LatestArticles)
admin.site.register(ContactUs)
admin.site.register(AboutUs)
