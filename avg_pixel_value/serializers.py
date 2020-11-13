from rest_framework import serializers

from avg_pixel_value.models import UploadedImage


class UploadedImageSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize an UploadedImage to and from Python objects."""

    class Meta:

        model = UploadedImage
        fields = ("image", "id", "created", "modified")
