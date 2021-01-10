# from django.db import models

# Create your models here.
# from django.db import models

# class Product(models.Model):
#
#   title = models.CharField(max_length=120)
#   description = models.TextField()
#   price = models.DecimalField(decimal_places=2,max_digits=40)

from django.db import models

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    # option_four= models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    # option_four_count = models.IntegerField(default=0)

    @classmethod
    def _delete_data(cls):  # this function deletes all the data
        Poll.objects.all().delete()

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count