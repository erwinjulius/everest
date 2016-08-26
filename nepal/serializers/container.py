# encoding: utf-8
from rest_framework import serializers

from nepal.models import Container


class ContainerSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Container
        fields = ('id', 'name', 'config')