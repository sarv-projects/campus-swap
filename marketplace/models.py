
from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name
class Item(models.Model):
    seller=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='items')
    title=models.CharField(max_length=200)
    description=models.CharField(help_text="Describe the item (working,defects,etc)")
    price=models.DecimalField(max_digits=7,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='item_images/',null=True,blank=True)
    condition=models.CharField(
        max_length=50,
        choices=[('New', 'New'), ('Used - Good', 'Used - Good'), ('Used - Fair', 'Used - Fair')],
        default='Used - Good'
    )
    purchase_date = models.DateField(null=True, blank=True, help_text="Original purchase date")
    created_at = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)  # track if item is sold
    def __str__(self):
        return f"{self.title} - {self.seller.username}"

class Order(models.Model):
    """
    Represents a purchase
    """
    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders'
    )
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.item.title} bought by {self.buyer.username}"