from rest_framework import serializers
from studentapp.models import Student

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
      model = Student
      fields = ['name', 'address', 'fee','id']