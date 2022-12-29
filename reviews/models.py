from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator




class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    stars = models.IntegerField(
            validators=[
                MinValueValidator(1),
                MaxValueValidator(5)
            ]
        )
    review = models.TextField()
    spoilers = models.BooleanField(null=True, blank=True, default=False)

    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews", default=""
    )

    critic = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews", default=""
    )

"""
 stars = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    OU

COM CHOICES
"""