import datetime
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.



class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # id = models.AutoField()
    USER_CHOICES = [
     ('Chairman', 'Chairman'),
     ('Principal', 'Principal'),
     ('HOD', 'HOD'),
     ('Mentor', 'Mentor'),
     ('Student', 'Student'),
    ]
    user_type = models.CharField(max_length=20, choices=USER_CHOICES)

class Chairman(UserProfile):
    name = models.CharField(max_length=30, default="")
    email = models.EmailField()





class College(models.Model):
    name = models.CharField(max_length=100)
    principal_name = models.CharField(max_length=30, default="")
    principal_email = models.EmailField()


class Principal(UserProfile):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="")
    email = models.EmailField()
    education = models.CharField(max_length=30, default="")

class Department(models.Model):
    department_title = models.CharField(max_length=30, default="")
    college = models.ForeignKey(College, on_delete=models.CASCADE, default="")
    department_hod_name = models.CharField(max_length=30, default="")
    number_of_semesters = models.IntegerField(MaxValueValidator(8), default=6)

class HOD(UserProfile):
    name = models.CharField(max_length=30, default="")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField()
    education = models.CharField(max_length=40)

    def _str_(self):
        return self.name


class Mentor(UserProfile):
    name = models.CharField(max_length=30, default="")
    email = models.EmailField()
    mentoring_class = models.CharField(max_length=30, default="")
    number_of_students = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)


class Hobby(models.Model):
    title = models.CharField(max_length=10)

    def _str_(self):
        return self.title
    
class Sports(models.Model):
    sport_title = models.CharField(max_length=20)

    def _str_(self):
        return self.sport_title

class Student(models.Model):
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female')
    ]
    NATIONALITY_CHOICES = [
        ('CANADA', 'Canada'),
        ('USA', 'Usa'),
        ('INDIA', 'India')
    ]
    
    name = models.CharField(max_length=20)
    study_semester = models.IntegerField(default=1)
    enrollment = models.CharField(max_length=30, unique=True, default="", null=False, blank=False)
    student_photo = models.ImageField()
    father_name = models.CharField(max_length=30, default="")
    father_photo = models.ImageField()
    mother_name = models.CharField(max_length=30, default="")
    mother_photo = models.ImageField()
    mentoring_started_year = models.DateField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    division = models.CharField(max_length=2)
    email = models.EmailField()
    caste = models.CharField(max_length=30, default="")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    weight = models.IntegerField()
    height = models.IntegerField()
    address = models.TextField()
    date_of_birth = models.DateField(default=datetime.datetime.now)
    mentor_name = models.CharField(max_length=30, default="")
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    pincode = models.IntegerField()
    hobbies = models.ManyToManyField(Hobby)
    nationality = models.CharField(max_length=10, choices=NATIONALITY_CHOICES)
    sport = models.ManyToManyField(Sports)
    overall_10th = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(100)], max_digits=10, decimal_places=3, null=True)
    overall_12th = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(100)], max_digits=10, decimal_places=3, null=True)
    diploma = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(100)], max_digits=10, decimal_places=3, null=True)
    student_contact = PhoneNumberField(null=False, default="+91")
    father_contact = PhoneNumberField(null=False, default="+91")
    mother_contact = PhoneNumberField(null=False, default="+91")
    father_occupation = models.CharField(max_length=20, default="")
    mother_occupation = models.CharField(max_length=20, default="")
    attendence = models.IntegerField(null=True, blank=True, default="")
    spi = models.IntegerField(null=True, blank=True, default=0)
    cpi = models.IntegerField(null=True, blank=True, default=0)
    fees_paid = models.IntegerField(null=True, blank=True, default=0)
    activity = models.JSONField(default='')
    project = models.JSONField(default='')
    membership_in_organization = models.JSONField(default='')
    fees_unpaid = models.IntegerField(default=60000)

    def _str_(self):
        return self.name


class Subject(models.Model):
    subject_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=20)
    subject_semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def _str_(self):
        return self.subject_name

class Result(models.Model):
    semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    type_of_exam = models.CharField(max_length=255, default="")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    currriculum_year = models.IntegerField(default=0)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    marks = models.IntegerField(default=0)
    grade = models.CharField(max_length=30, default="")
    exam_year = models.IntegerField()

    def _str_(self):
        return self.student.name
    

class Feesproof(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.now)
    proof = models.FileField(upload_to="proof/")


# import datetime
# from django.db import models
# from django.contrib.auth.models import Group
# from django.contrib.auth.models import Permission
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField

# # Create your models here.



# class User(AbstractUser):
#     groups = models.ManyToManyField(Group, related_name='user_groups')
#     user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     # id = models.AutoField()
#     USER_CHOICES = [
#         ('Chairman', 'Chairman'),
#         ('Principal', 'Principal'),
#         ('HOD', 'HOD'),
#         ('Mentor', 'Mentor'),
#         ('Student', 'Student'),
#     ]
#     user_type = models.CharField(max_length=20, choices=USER_CHOICES)

# class Chairman(UserProfile):
#     name = models.CharField(max_length=30, default="")
#     email = models.EmailField()





# class College(models.Model):
#     name = models.CharField(max_length=100)
#     principal_name = models.CharField(max_length=30, default="")
#     principal_email = models.EmailField()


# class Principal(UserProfile):
#     college = models.ForeignKey(College, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30, default="")
#     email = models.EmailField()
#     education = models.CharField(max_length=30, default="")

# class Department(models.Model):
#     department_title = models.CharField(max_length=30, default="")
#     college = models.ForeignKey(College, on_delete=models.CASCADE, default="")
#     department_hod_name = models.CharField(max_length=30, default="")
#     number_of_semesters = models.IntegerField(MaxValueValidator(8), default=6)

# class HOD(UserProfile):
#     name = models.CharField(max_length=30, default="")
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     email = models.EmailField()
#     education = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


# class Mentor(UserProfile):
#     name = models.CharField(max_length=30, default="")
#     email = models.EmailField()
#     mentoring_class = models.CharField(max_length=30, default="")
#     number_of_students = models.IntegerField()
#     college = models.ForeignKey(College, on_delete=models.CASCADE, null=True)
#     department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)


# class Hobby(models.Model):
#     title = models.CharField(max_length=10)

#     def __str__(self):
#         return self.title
    
# class Sports(models.Model):
#     sport_title = models.CharField(max_length=20)

#     def __str__(self):
#         return self.sport_title

# class Student(models.Model):
#     GENDER_CHOICES = [
#         ('MALE', 'Male'),
#         ('FEMALE', 'Female')
#     ]
#     NATIONALITY_CHOICES = [
#         ('CANADA', 'Canada'),
#         ('USA', 'Usa'),
#         ('INDIA', 'India')
#     ]
    
#     name = models.CharField(max_length=20)
#     study_semester = models.IntegerField(default=1)
#     enrollment = models.CharField(max_length=30, unique=True, default="", null=False, blank=False)
#     student_photo = models.ImageField()
#     father_name = models.CharField(max_length=30, default="")
#     father_photo = models.ImageField()
#     mother_name = models.CharField(max_length=30, default="")
#     mother_photo = models.ImageField()
#     mentoring_started_year = models.DateField(auto_now_add=True)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
#     division = models.CharField(max_length=2)
#     email = models.EmailField()
#     caste = models.CharField(max_length=30, default="")
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
#     weight = models.IntegerField()
#     height = models.IntegerField()
#     address = models.TextField()
#     mentor_name = models.CharField(max_length=30, default="")
#     city = models.CharField(max_length=15)
#     state = models.CharField(max_length=15)
#     pincode = models.IntegerField()
#     hobbies = models.ManyToManyField(Hobby)
#     nationality = models.CharField(max_length=10, choices=NATIONALITY_CHOICES)
#     sport = models.ManyToManyField(Sports)
#     overall_10th = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(100)], max_digits=10, decimal_places=3, null=True)
#     overall_12th = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(100)], max_digits=10, decimal_places=3, null=True)
#     diploma = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(100)], max_digits=10, decimal_places=3, null=True)
#     student_contact = PhoneNumberField(null=False, default="+91")
#     father_contact = PhoneNumberField(null=False, default="+91")
#     mother_contact = PhoneNumberField(null=False, default="+91")
#     father_occupation = models.CharField(max_length=20, default="")
#     mother_occupation = models.CharField(max_length=20, default="")
#     attendence = models.IntegerField(null=True, blank=True, default="")
#     spi = models.IntegerField(null=True, blank=True, default=0)
#     cpi = models.IntegerField(null=True, blank=True, default=0)
#     fees_paid = models.IntegerField(null=True, blank=True, default=0)
#     fees_unpaid = models.IntegerField(default=60000)

#     def __str__(self):
#         return self.name


# class Subject(models.Model):
#     subject_code = models.CharField(max_length=10)
#     subject_name = models.CharField(max_length=20)
#     subject_semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.subject_name

# class Result(models.Model):
#     semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
#     type_of_exam = models.CharField(max_length=255, default="")
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     currriculum_year = models.IntegerField(default=0)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
#     marks = models.IntegerField(default=0)
#     grade = models.CharField(max_length=30, default="")
#     exam_year = models.IntegerField()

#     def __str__(self):
#         return self.student.name
    

# class Feesproof(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     amount = models.IntegerField(default=0)
#     date = models.DateField(default=datetime.datetime.now)
#     proof = models.FileField(upload_to="proof/")
    
    
    
    