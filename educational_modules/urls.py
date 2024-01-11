from rest_framework import permissions
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import path
from educational_modules.apps import EducationalModulesConfig
from educational_modules.views import EducationListAPIView, EducationCreateAPIView, EducationRetrieveAPIView, \
    EducationUpdateAPIView, EducationDestroyAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


app_name = EducationalModulesConfig.name


urlpatterns = [
    path('', EducationListAPIView.as_view(), name='lesson_list'),
    path('create/', EducationCreateAPIView.as_view(), name='lesson-create'),
    path('retrieve/<int:pk>/', EducationRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('update/<int:pk>/', EducationUpdateAPIView.as_view(), name='lesson-update'),
    path('delete/<int:pk>/', EducationDestroyAPIView.as_view(), name='lesson-delete'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
