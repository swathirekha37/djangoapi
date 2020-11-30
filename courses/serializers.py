from rest_framework import serializers
from .models import Course

#in order to create api's we should have serializers.
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id','url','name','language','price')