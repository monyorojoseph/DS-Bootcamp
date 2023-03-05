from rest_framework import viewsets
from rest_framework import mixins
from django.db import transaction
from rest_framework.exceptions import APIException
from .serializers import *
from .models import *

class EndpointViewset(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = EndpointSerializer
    queryset = Endpoint.objects.all()

class MLAlgorithmViewset(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithm.objects.all()

def deactivate_other_status(instance):
    old_status = MLAlgorithmStatus.objects.filter(parent_mlalgorithm=instance.parent_mlalgorithm,
                                                  created_at__lt=instance.created_at,
                                                  active=True)

    for i in range(len(old_status)):
        old_status[i].active = False
    MLAlgorithmStatus.objects.bulk_update(old_status, ['active'])


class MLAlgorithmStatusViewset(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.CreateModelMixin):
    serializer_class = MLAlgorithmStatusSerializer
    queryset = MLAlgorithmStatus.objects.all()

    def perform_create(self, serializer):
        # return super().perform_create(serializer)
        try:
            with transaction.atomic():
                instance = serializer.save(active=True)
                deactivate_other_status(instance)
        except Exception as e:
            raise APIException(str(e))


class MLRequestViewset(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.UpdateModelMixin):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()