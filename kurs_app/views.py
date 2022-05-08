from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render
from rest_framework import status, request
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Teacher,Student,Content,Course,Comment,Royxat,Video
from .serializers import TeacherSerializer,StudentSerializer,CommentSerializer,CourseSerializer,ContentSerializer,RoyxatSerializer,VideoSerializer


class TeacherAPIView(ListCreateAPIView):

    serializer_class = TeacherSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        teach = Teacher.objects.filter(user=self.request.user)
        return teach


class TeacherRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        teach = Teacher.objects.filter(user=self.request.user)
        return teach


class StudentAPIView(ListCreateAPIView):
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student = Student.objects.filter(user=self.request.user)
        return student



class StudentRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student = Student.objects.filter(user=self.request.user)
        return student

class CourseAPI(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["name"]

class CourseAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        malumot = CourseSerializer(courses, many=True)
        return Response(malumot.data)

    def get_queryset(self):
        course = Course.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            course = Course.objects.annotate(
                similarity=TrigramSimilarity("name", soz)
            ).filter(similarity__gte=1).order_by("-similarity")
        return course

    def post(self, request):
        tech = Teacher.objects.filter(user=request.user)
        ser = CourseSerializer(data=request.data)
        if tech.approved :
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)



# class StudentDashboard(ListCreateAPIView):
#     student = Student.objects.filter(user=request.user)
#     queryset = Royxat.objects.filter(student=student)
#     serializer_class = RoyxatSerializer

class TeacherDashboard(APIView):
    def get(self, request):
        tech = Teacher.objects.filter(user=request.user)
        course = Course.objects.filter(teacher=tech)
        royxat = Royxat.objects.filter(course=course).count()
        malumot = CourseSerializer(tech, many=True)
        return Response(malumot.data,royxat.data)

class ContentAPIView(ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class CommentAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RoyxatAPIView(ListCreateAPIView):
    queryset = Royxat.objects.all()
    serializer_class = RoyxatSerializer

class VideoAPIView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
