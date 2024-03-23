# Generated by Django 5.0.2 on 2024-03-09 14:31

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('principal_name', models.CharField(default='', max_length=30)),
                ('principal_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_name='user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_title', models.CharField(default='', max_length=30)),
                ('department_hod_name', models.CharField(default='', max_length=30)),
                ('number_of_semesters', models.IntegerField(default=6, verbose_name=django.core.validators.MaxValueValidator(8))),
                ('college', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.college')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('study_semester', models.IntegerField(default=1)),
                ('enrollment', models.CharField(default='', max_length=30, unique=True)),
                ('student_photo', models.ImageField(upload_to='')),
                ('father_name', models.CharField(default='', max_length=30)),
                ('father_photo', models.ImageField(upload_to='')),
                ('mother_name', models.CharField(default='', max_length=30)),
                ('mother_photo', models.ImageField(upload_to='')),
                ('mentoring_started_year', models.DateField(auto_now_add=True)),
                ('division', models.CharField(max_length=2)),
                ('email', models.EmailField(max_length=254)),
                ('caste', models.CharField(default='', max_length=30)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=10)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('address', models.TextField()),
                ('mentor_name', models.CharField(default='', max_length=30)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=15)),
                ('pincode', models.IntegerField()),
                ('nationality', models.CharField(choices=[('CANADA', 'Canada'), ('USA', 'Usa'), ('INDIA', 'India')], max_length=10)),
                ('overall_10th', models.DecimalField(decimal_places=3, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('overall_12th', models.DecimalField(decimal_places=3, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('diploma', models.DecimalField(decimal_places=3, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('student_contact', phonenumber_field.modelfields.PhoneNumberField(default='+91', max_length=128, region=None)),
                ('father_contact', phonenumber_field.modelfields.PhoneNumberField(default='+91', max_length=128, region=None)),
                ('mother_contact', phonenumber_field.modelfields.PhoneNumberField(default='+91', max_length=128, region=None)),
                ('father_occupation', models.CharField(default='', max_length=20)),
                ('mother_occupation', models.CharField(default='', max_length=20)),
                ('attendence', models.IntegerField(blank=True, default='', null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.department')),
                ('hobbies', models.ManyToManyField(to='api.hobby')),
                ('sport', models.ManyToManyField(to='api.sports')),
            ],
        ),
        migrations.CreateModel(
            name='Feesproof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('proof', models.FileField(upload_to='proof/')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=10)),
                ('subject_name', models.CharField(max_length=20)),
                ('subject_semester', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.department')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('grade', models.CharField(default='', max_length=30)),
                ('exam_year', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subject')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.user')),
                ('user_type', models.CharField(choices=[('CHAIRMAN', 'Chairman'), ('PRINCIPAL', 'Principal'), ('HOD', 'HOD'), ('MENTOR', 'Mentor'), ('STUDENT', 'Student')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.userprofile')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
            bases=('api.userprofile',),
        ),
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.userprofile')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('education', models.CharField(max_length=40)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.department')),
            ],
            bases=('api.userprofile',),
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.userprofile')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mentoring_class', models.CharField(default='', max_length=30)),
                ('number_of_students', models.IntegerField()),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.department')),
            ],
            bases=('api.userprofile',),
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.userprofile')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('education', models.CharField(default='', max_length=30)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.college')),
            ],
            bases=('api.userprofile',),
        ),
    ]