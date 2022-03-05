from rest_framework import serializers
from test.models import Actual_work


class Actual_workSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actual_work
        fields = "__all__"
