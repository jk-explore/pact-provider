from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return a group instance

    create:
    Create a new group.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def provider_states(request, state):
    if request.method == 'POST':
        prov_state = request
        if prov_state == "admin exists and is not an administrator":
            data = "{\"username\":\"admin\", \"email\":\"admin@dev.net\"}"
            serializer = UserSerializer(data=data)
            serializer.save()

