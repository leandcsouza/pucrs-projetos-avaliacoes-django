from rest_framework.permissions import DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sala
from .serializers import SalaSerializer


class SalaView(APIView):
    permission_classes = []

    def get_queryset(self):
        return Sala.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        serializer = SalaSerializer(queryset, many=True)
        return Response(serializer.data)
