from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django_filters import rest_framework as filters

from todo.models import Task, Project, Sprint
from todo.api.serializers import TaskSerializer, ProjectSerializer, \
    SprintSerializer
from todo.api.permissions import isAssigneeOrReadOnly

User = get_user_model()


class TaskFilter(filters.FilterSet):
    class Meta:
        model = Task
        fields = ['project']


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (isAssigneeOrReadOnly,)
    filter_class = TaskFilter

    def create(self, request, *args, **kwargs):
        copy_data = request.data.copy()
        copy_data['creator'] = request.user.pk
        assignee_ids = request.data.getlist('assignees[]', [])
        serializer = self.get_serializer(data=copy_data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        # http://stackoverflow.com/questions/37511421/add-an-object-by-id-in-a-manytomany-relation-in-django
        assignees = User.objects.filter(id__in=assignee_ids)

        serializer.instance.assignees = assignees

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
