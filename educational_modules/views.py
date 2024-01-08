from rest_framework import generics

from educational_modules.models import Lessons
from educational_modules.serializers import LessonsSerializer


class EducationCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonsSerializer


class EducationListAPIView(generics.ListAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class EducationRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class EducationUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class EducationDestroyAPIView(generics.DestroyAPIView):
    queryset = Lessons.objects.all()
