import numpy as np
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from skimage import io, img_as_float

from avg_pixel_value.models import UploadedImage
from avg_pixel_value.serializers import UploadedImageSerializer


class UploadedImageViewSet(viewsets.ModelViewSet):
    """REST endpoint for UploadedImage instances.

    Provides all CRUD methods.
    """

    serializer_class = UploadedImageSerializer
    queryset = UploadedImage.objects.all()


@api_view(["GET"])
def calculate_avg_pixel_value(request: Request, pk: int) -> Response:
    """Calculate the average pixel value of an UploadedImage."""

    uploaded_image = get_object_or_404(UploadedImage, pk=pk)
    image = io.imread(uploaded_image.image.name)

    # Optional step to return a value between 0 and 1.
    image = img_as_float(image)

    # Return the mean of all pixels
    return Response(float(np.mean(image)))
