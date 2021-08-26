from django.db import models

# Create your models here.


ITEMS = (
	('Laptop', 'Laptop'),
	('Keyboard', 'Keyboard'),
	('Mouse', 'Mouse'),
	('Headphone', 'Headphone'),
)


class Cart(models.Model):
	user = models.ForeignKey('core.User', on_delete=models.PROTECT)
	item = models.CharField(max_length=25, choices=ITEMS)
	price = models.FloatField()
	date = models.DateTimeField(auto_now_add=True)
	ordered = models.BooleanField(default=False)
