from . serializers import ToDoSerializer
from .models import ToDo
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class ToDoListApi(ListCreateAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)


class ToDoEditAndDeleteApi(RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)
