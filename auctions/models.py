from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction(models.Model):
    title = models.CharField(max_length=128)
    start_price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=256)
    image_url = models.URLField()
    #listed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")

    def __str__(self):
        return self.title


# class Bid(models.Model):
#     date_created = models.DateTimeField(auto_now_add=True)
#     auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='auction_id')
#     bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bidder')
#     bid_amount = models.FloatField()
#
#     def __str__(self):
#         return self.id

