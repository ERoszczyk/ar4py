from datetime import datetime

from django.shortcuts import render
from django.utils import timezone
from django.views import View
from rest_framework import permissions, status, serializers
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


class AppointmentCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100, required=True)
    last_name = serializers.CharField(max_length=100, required=True)
    date = serializers.DateTimeField(required=True)

    class Meta:
        fields = ["first_name", "last_name", "date"]

    def create(self, validated_data):
        student_data = {"first_name": validated_data.pop('first_name'), "last_name": validated_data.pop("last_name")}
        student, created = Student.objects.get_or_create(**student_data)
        return Appointment.objects.create(student=student, **validated_data)


class AppointmentSerializer(ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentsViewSet(ModelViewSet):
    queryset = Appointment.objects.all()

    def get_serializer_class(self):
        return AppointmentCreateSerializer if self.action == 'create' else AppointmentSerializer

    @action(detail=False, methods=['get'])
    def next(self, request):
        obj = self.queryset.filter(is_active=True).order_by('date').first()
        print(obj)
        if obj:
            response = Response({"next_appointment": self.get_serializer_class()(obj).data}, status.HTTP_200_OK)
            obj.is_active = False
            obj.save()
        else:
            response = Response({"msg": 'No more appointments'}, status.HTTP_400_BAD_REQUEST)
        return response

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response({'msg': obj.id}, status=status.HTTP_201_CREATED)
