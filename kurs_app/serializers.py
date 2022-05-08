from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from kurs_app.models import Teacher,Student,Content,Course,Comment,Royxat,Video


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    def validated_name(self, qiymat):
        if len(qiymat) <= 2:
            raise ValidationError(detail="Siz ikkidona harf kiritingiz")
        return qiymat



class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
    def validate_videp(self, qiymat):
        if not qiymat.endswith(".mp4") or qiymat.endswith(".3gp"):
            raise ValidationError(detail="Bunaqa video formati yoq")
        return qiymat

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class RoyxatSerializer(ModelSerializer):
    class Meta:
        model = Royxat
        fields = '__all__'