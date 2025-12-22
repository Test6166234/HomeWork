from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Doctor, Patient, Branch, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(help_text="Имя врача (например: Иван Петров)")
    specialization = serializers.CharField(
        help_text="Специализация врача (например: терапевт, хирург)"
    )
    phone_number = serializers.CharField(help_text="Телефон (например: +996777777777)")

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'phone_number', 'is_active', 'branch']
        read_only_fields = ['id', 'is_active']

class PatientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(help_text="Имя пациента")
    status = serializers.CharField(help_text="Статус: sick/healthy")

    class Meta:
        model = Patient
        fields = ['id', 'name', 'status']
        read_only_fields = ['id']

class BranchSerializer(serializers.ModelSerializer):
    name = serializers.CharField(help_text="Название филиала")
    address = serializers.CharField(help_text="Адрес филиала")

    class Meta:
        model = Branch
        fields = ['id', 'name', 'address', 'is_active']
        read_only_fields = ['id']

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all(), help_text="ID врача"
    )
    patient = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), help_text="ID пациента"
    )
    date = serializers.DateTimeField(help_text="Дата/время приёма")

    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'patient', 'date']
        read_only_fields = ['id']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, help_text="Пароль (не возвращается в ответе)"
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
