from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from kurs_app.views import TeacherDashboard,CourseAPI,TeacherAPIView,TeacherRUD,StudentAPIView,StudentRUD,CourseAPIView,ContentAPIView,CommentAPIView,RoyxatAPIView,VideoAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TeacherAPIView.as_view() ),
    path('techrud/<int:pk>/', TeacherRUD.as_view() ),
    path('student/', StudentAPIView.as_view() ),
    path('studentrud/<int:pk>/', StudentRUD.as_view() ),
    path('course/', CourseAPIView.as_view() ),
    path('courses/', CourseAPI.as_view() ),
    path('teacherdash/', TeacherDashboard.as_view() ),
    # path('studentdash/', StudentDashboard.as_view() ),
    path('content/', ContentAPIView.as_view() ),
    path('comment/', CommentAPIView.as_view() ),
    path('royxat/', RoyxatAPIView.as_view() ),
    path('video/', VideoAPIView.as_view() ),
    path('get-token/', obtain_auth_token),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)