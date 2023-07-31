import char as char
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from pure_pagination import Paginator, PageNotAnInteger
from courses.models import Courses, Teachers, PeopleSay, LatestArticles, ContactUs, AboutUs


# Create your views here.
class IndexView(View):
    def get(self, request):
        courses_data = Courses.objects.filter(course_active=True).order_by('course_order')
        print("Courses...", courses_data)

        teachers_data = Teachers.objects.filter(teacher_active=True).order_by('teacher_order')
        print("Teachers...", teachers_data)

        what_people_say_data = PeopleSay.objects.all()
        print("What People Say...", what_people_say_data)

        latest_articles_data = LatestArticles.objects.all()
        print("Latest Articles...", latest_articles_data)

        return render(request, "index.html", {'courses_data_k': courses_data, 'teachers_data_k': teachers_data,
                                              'what_people_say_data_k': what_people_say_data,
                                              'latest_articles_data_k': latest_articles_data})


class ContactUsView(View):
    def get(self, request):
        return render(request, 'contact.html')


class AboutUsView(View):
    def get(self, request):
        what_people_say_data = PeopleSay.objects.all()
        print("What People Say...", what_people_say_data)

        about_us_data = AboutUs.objects.all()
        print("AboutUs...", about_us_data)

        teachers_data = Teachers.objects.filter(teacher_active=True).order_by('teacher_order')
        print("Teachers...", teachers_data)

        return render(request, 'about.html',
                      {'what_people_say_data_k': what_people_say_data, 'teachers_data_k': teachers_data,
                       'about_us_data_k': about_us_data})

    def post(self, request):
        fname = request.POST.get('f_name')
        lname = request.POST.get('l_name')
        email = request.POST.get('email')
        phone = request.POST.get('phn_num')
        msg = request.POST.get('msg')

        ContactUs.objects.create(f_name=fname, l_name=lname, email=email, phone_number=phone, msg=msg)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class CoursesView(View):
    def get(self, request):
        courses_data = Courses.objects.filter(course_active=True).order_by('course_order')
        # courses_data = Courses.objects.all()
        print("Courses View...", courses_data)

        try:
            page = request.GET.get('page', 1)
            print("URL page number..", page)
        except PageNotAnInteger:
            page = 1
        p = Paginator(courses_data, 2, request=request)
        courses_paginated_data = p.page(page)

        return render(request, 'courses.html', {'courses_paginated_data_k': courses_paginated_data})
