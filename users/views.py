from datetime import datetime

from django.shortcuts import render
from django.utils import timezone
from django.views import View
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.models import Appointment, Student


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class AppointmentSerializer(ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        student_data = validated_data.pop('student')
        student, created = Student.objects.get_or_create(**student_data)
        return Appointment.objects.create(student=student, **validated_data)


class AppointmentsViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

    @action(detail=False, methods=['get'])
    def next(self, request):
        # print(self.request.query_params) Maybe we will need to add here authorization
        obj = self.queryset.filter(date__gte=timezone.localtime(timezone.now()).first())
        return Response({"next_appointment": self.serializer_class(obj).data}, status.HTTP_200_OK)
