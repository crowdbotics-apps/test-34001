from rest_framework import authentication
from test.models import Actual_work
from .serializers import Actual_workSerializer
from rest_framework import viewsets


class Actual_workViewSet(viewsets.ModelViewSet):
    serializer_class = Actual_workSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Actual_work.objects.all()
