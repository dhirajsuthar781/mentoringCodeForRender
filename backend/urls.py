"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function viewsl
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path('', TemplateView.as_view(template_name='index.html')),
    path('', TemplateView.as_view(template_name='index.html')),
    path("Signup", TemplateView.as_view(template_name='index.html')),
    path("Testing", TemplateView.as_view(template_name='index.html')),
    path("dashboard", TemplateView.as_view(template_name='index.html')),
    path("attendanceitem", TemplateView.as_view(template_name='index.html')),
    path("attendance", TemplateView.as_view(template_name='index.html')),
    path("beee", TemplateView.as_view(template_name='index.html')),
    path("fme", TemplateView.as_view(template_name='index.html')),
    path("eg", TemplateView.as_view(template_name='index.html')),
    path("civil", TemplateView.as_view(template_name='index.html')),
    path("physics", TemplateView.as_view(template_name='index.html')),
    path("attendance", TemplateView.as_view(template_name='index.html')),
    path("results", TemplateView.as_view(template_name='index.html')),
    path("fees", TemplateView.as_view(template_name='index.html')),
    path("university", TemplateView.as_view(template_name='index.html')),
    path("notification", TemplateView.as_view(template_name='index.html')),
    
    path("student", TemplateView.as_view(template_name='index.html')),
    path("info", TemplateView.as_view(template_name='index.html')),
    path("history", TemplateView.as_view(template_name='index.html')),
    path("exam", TemplateView.as_view(template_name='index.html')),
    path("midsem", TemplateView.as_view(template_name='index.html')),
    path("activity", TemplateView.as_view(template_name='index.html')),
    path("seminar", TemplateView.as_view(template_name='index.html')),
    path("mentorshipitem", TemplateView.as_view(template_name='index.html')),
    
    path("mentorship", TemplateView.as_view(template_name='index.html')),
    path("attendancementorship", TemplateView.as_view(template_name='index.html')),
    path("resultsmentorship", TemplateView.as_view(template_name='index.html')),
    path("feesmentorship", TemplateView.as_view(template_name='index.html')),
    path("sessionmentorship", TemplateView.as_view(template_name='index.html')),
    path("mentorship/mentoringform", TemplateView.as_view(template_name='index.html')),
    path("attendancementorship/attendancementorshiptable", TemplateView.as_view(template_name='index.html')),
    path("resultsmentorship/mentorshipresults", TemplateView.as_view(template_name='index.html')),
    path("feesmentorship/mentorshipfees", TemplateView.as_view(template_name='index.html')),
    path("mentorship/attendancesheet", TemplateView.as_view(template_name='index.html')),
    path("mentorship/university", TemplateView.as_view(template_name='index.html')),
    
    path("hod", TemplateView.as_view(template_name='index.html')),
    path("attendancehod", TemplateView.as_view(template_name='index.html')),
    path("resultshod", TemplateView.as_view(template_name='index.html')),
    path("feeshod", TemplateView.as_view(template_name='index.html')),
    path("cards", TemplateView.as_view(template_name='index.html')),
    path("dashod", TemplateView.as_view(template_name='index.html')),
    path("hod/hodform", TemplateView.as_view(template_name='index.html')),
    path("hod/detailshod", TemplateView.as_view(template_name='index.html')),
    path("attendancehod/attendancetablehod", TemplateView.as_view(template_name='index.html')),
    path("resultshod/resultstablehod", TemplateView.as_view(template_name='index.html')),
    path("feeshod/feestablehod", TemplateView.as_view(template_name='index.html')),
    path("dashod/chat", TemplateView.as_view(template_name='index.html')),
    path("hod/classcards", TemplateView.as_view(template_name='index.html')),
    path("attendancehod/attendancehoddetails", TemplateView.as_view(template_name='index.html')),
    path("feeshod/feeshoddetails", TemplateView.as_view(template_name='index.html')),
    path("resultshod/resultshoddetails", TemplateView.as_view(template_name='index.html')),

    path("principle", TemplateView.as_view(template_name='index.html')),
    path("principle/mentorsofDepartment", TemplateView.as_view(template_name='index.html')),
    path("principle/mentorsForm", TemplateView.as_view(template_name='index.html')),
    path("attendanceprinciple", TemplateView.as_view(template_name='index.html')),
    path("attendanceprinciple/mentorsforAttend", TemplateView.as_view(template_name='index.html')),
    path("attendanceprinciple/mentorsAttendence", TemplateView.as_view(template_name='index.html')),
    path("resultspriciple", TemplateView.as_view(template_name='index.html')),
    path("resultspriciple/mentorsResultPriciple", TemplateView.as_view(template_name='index.html')),
    path("resultspriciple/resultDetailsPriciple", TemplateView.as_view(template_name='index.html')),
    path("feesprinciple", TemplateView.as_view(template_name='index.html')),
    path("feesprinciple/mentorsFeesPrinciple", TemplateView.as_view(template_name='index.html')),
    path("feesprinciple/FessDetailsPriciple", TemplateView.as_view(template_name='index.html')),
    path("universityprinciple", TemplateView.as_view(template_name='index.html')),
    path("dashprinciple", TemplateView.as_view(template_name='index.html')),
    path("dashprinciple/chat", TemplateView.as_view(template_name='index.html')),
    
    path("chairmain", TemplateView.as_view(template_name='index.html')),
    path("chairmain/chairmainhome", TemplateView.as_view(template_name='index.html')),
    path("notificationchairmain", TemplateView.as_view(template_name='index.html')),
]
