from django.db import models

from . import top


class Post(models.Model):
    param1 = models.FloatField(max_length=10)
    param2 = models.FloatField(max_length=10)
    param3 = models.FloatField(max_length=10)
    epsilon = models.FloatField(max_length=10)
    nums = models.FloatField(max_length=10)

    def publish(self):
        self.save()

    def __str__(self):
        top.main(top.f, self.param1, self.param2, self.param3, self.nums)
        return "y = {}x^2 + {}x + {}".format(self.param1, self.param2, self.param3)
