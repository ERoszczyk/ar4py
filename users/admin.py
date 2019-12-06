from django.contrib import admin
from django.contrib.auth import get_user_model

from users.models import Appointment, Student

User = get_user_model()


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
