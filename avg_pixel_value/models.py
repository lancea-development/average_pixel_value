from django.db import models
from model_utils.models import TimeStampedModel


class UploadedImage(TimeStampedModel):
    """An Image uploaded to the database."""

    image = models.FileField(upload_to="images/")

    def __repr__(self) -> str:
        """String representation of the image instance."""
        return f"{self.id} created: {self.created.strftime('%Y-%m-%d %H:%M')}"
