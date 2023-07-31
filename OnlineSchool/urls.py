from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import IndexView, ContactUsView, AboutUsView, CoursesView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^$', IndexView.as_view(), name='index'),
                  url(r'^contact_us/$', ContactUsView.as_view(), name='contact_us'),
                  url(r'^about_us/$', AboutUsView.as_view(), name='about_us'),
                  url(r'^courses/$', CoursesView.as_view(), name='courses'),
                  url(r'^form/$', AboutUsView.as_view(), name='form'),

                  # path('courses/', include('courses.urls')),  # here 'courses/' is app_name
                  # path('blogs/', include('blogs.urls'))  # here 'blogs/' is app_name
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
