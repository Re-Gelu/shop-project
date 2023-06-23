from config.permissions import ReadOnly
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .serializers import GroupSerializer

# ViewSets


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [ReadOnly | IsAdminUser, ]
