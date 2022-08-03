import uuid

from EMS_app import serializers
from EMS_app import models

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class RegistrationAPIView(generics.GenericAPIView):
    """Api view for registration"""
    
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId":str(uuid.uuid4()),
                "Message":"User created successfully",
                "User":serializer.data
            },status=status.HTTP_201_CREATED)

        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


class ListCategory(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class ListUser(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class ListStudent(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

class ListCourse(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class DetailCourse(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class ListEnquiry(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Enquiry.objects.all()
    serializer_class = serializers.EnquirySerializer

class DetailEnquiry(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Enquiry.objects.all()
    serializer_class = serializers.EnquirySerializer
