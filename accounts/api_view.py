from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from . serializers import UserSreialzier


class ProfileApi(RetrieveUpdateAPIView):
    serializer_class = UserSreialzier
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    