from django.urls import path
from . import views

urlpatterns = [
    path('import_from_excel/', views.import_from_excel, name='import_from_excel'),
    path('signup/', views.signup, name='signup'),
    path('studentsmentor/', views.students_mentor, name='students_mentor'),
    path('uploadfile/', views.upload_file, name='upload_file'),
    path('fesscheck/', views.fess_check, name='fess_check'),
    path('students/', views.students, name='students'),
    path('login/', views.signin, name='login'),
    path("colleges/", views.colleges, name='colleges'),
    path("result/", views.result, name='result'),
    path("department/", views.departments, name='department'),
    path("mentors/", views.mentors, name='mentors'),
    path("mentorshipForm/", views.addStudent, name='MentorData'),
    path("resultExcel/", views.resultExcel, name='resultExcel'),
]
