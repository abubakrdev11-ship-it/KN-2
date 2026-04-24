from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='reviews')
    buyer = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='reviews_written')
    seller = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='reviews_received')
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
