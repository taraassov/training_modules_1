from django.urls import path
from educational_modules.apps import EducationalModulesConfig
from educational_modules.views import EducationListAPIView, EducationCreateAPIView, EducationRetrieveAPIView, \
    EducationUpdateAPIView, EducationDestroyAPIView


app_name = EducationalModulesConfig.name


urlpatterns = [
    path('', EducationListAPIView.as_view(), name='lesson_list'),
    path('create/', EducationCreateAPIView.as_view(), name='lesson-create'),
    path('retrieve/<int:pk>/', EducationRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('update/<int:pk>/', EducationUpdateAPIView.as_view(), name='lesson-update'),
    path('delete/<int:pk>/', EducationDestroyAPIView.as_view(), name='lesson-delete'),
]
