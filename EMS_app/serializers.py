from rest_framework import serializers
from EMS_app import models


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""
    email = serializers.EmailField(max_length = 50, min_length=6)
    username = serializers.CharField(max_length=255, min_length=6)
    password = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = models.CustomUser
        fields = ('id','first_name','last_name','email','username','password')

    def validate(self, attrs):
        email = attrs.get('email',None)
        username = attrs.get('username',None)
        if models.CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if models.CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('username already exists')})

        return super().validate(attrs)

    def create(self, validated_data):
        return models.CustomUser.objects.create_user(**validated_data)
      

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = (
            'id',
            'username',
            'email',
            'user_type'
        )


class CategorySerializer(serializers.ModelSerializer):
    """Serializer class for Category model"""
    class Meta:
        model = models.Category
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """Serializer class for Course model"""
    class Meta:
        model = models.Course
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    """Serializer class for Student serializer"""
    class Meta:
        model = models.Student
        fields = "__all__"


class EnquirySerializer(serializers.ModelSerializer):
    """Serializer class for Enquiry model"""
    class Meta:
        model = models.Enquiry
        fields = "__all__"