from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='reviews')
    buyer = models.ForeignKey('user.User', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Review by {self.buyer.username} - {self.rating}"