from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, \
    RetrieveUpdateDestroyAPIView

from .models import Content
from .permissions import IsOwner
from .serializers import ContentSerializer

from .extras import generate_random_token



class ContentCreateView(CreateAPIView):
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        token=generate_random_token()
        serializer.save(token=token, owner=self.request.user)


class ContentUpdateView(UpdateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = "token"


class ContentRetrieveView(RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    authentication_classes = []
    permission_classes = [AllowAny]
    lookup_field = "token"


class ContentDeleteView(DestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = "token"

class RUDView(RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = "token"

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsOwner()]
        return [IsAuthenticated()]
    def get_authenticators(self):
        if self.request.method == 'GET':
            return []
        return [SessionAuthentication(), BasicAuthentication(), TokenAuthentication()]

