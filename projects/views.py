from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import permissions

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAdminUser]
