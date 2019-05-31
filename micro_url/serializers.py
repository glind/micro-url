from rest_framework import serializers

from . import models


class URLServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.URLService
        fields = '__all__'
        read_only_fields = ( 'url_uuid', )

