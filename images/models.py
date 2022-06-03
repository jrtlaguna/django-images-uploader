from django.conf import settings
from django.db import models


class Image(models.Model):
    class ImageStatus(models.TextChoices):
        ACTIVE = ("ACTIVE", "ACTIVE")
        ARCHIVED = ("ARCHIVED", "ARCHIVED")
        DELETED = ("DELETED", "DELETED")

    image = models.ImageField(
        "Image",
        null=True,
        blank=True,
    )
    status = models.CharField(
        verbose_name="Status",
        max_length=30,
        choices=ImageStatus.choices,
        default=ImageStatus.ACTIVE,
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
