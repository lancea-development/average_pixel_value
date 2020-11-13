import string
import random
from io import BytesIO
from typing import Any

import pytest
from django.core.files import File
from rest_framework import status
from rest_framework.reverse import reverse

from PIL import Image
from rest_framework.test import APIClient


@pytest.fixture()
def api_client() -> APIClient:
    """Return an APIClient."""
    client = APIClient()
    return client


@pytest.fixture()
def image_file(tmpdir_factory: Any) -> File:
    """Return a simple image file."""
    file_obj = BytesIO()
    img = Image.new("RGB", (60, 30), color="red")
    img.save(file_obj, "png")
    file_obj.seek(0)
    return File(file_obj, name="test.png")


@pytest.mark.django_db
def test_avg_pixel_value(api_client: APIClient, image_file: File) -> None:
    """Test that the average pixel value is calculated properly."""
    url = reverse("image-list")
    response = api_client.post(url, data={"image": image_file})
    assert response.status_code == status.HTTP_201_CREATED

    pixel_value_url = reverse("pixelvalue", kwargs={"pk": response.data["id"]})
    pixel_value_response = api_client.get(pixel_value_url)
    assert pixel_value_response.status_code == status.HTTP_200_OK
    assert pixel_value_response.data == 0.3333333333333333
