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
        self.left, self.right = top.main(top.f, self.param1, self.param2, self.param3, self
                                         .nums, self.epsilon)
        return "y = {}x^2 + {}x + {} \n {} \n {}".format(self.param1, self.param2, self.param3, self.left, self.right)


class Images(models.Model):
    image = models.ImageField()

    def publish(self):
        self.save()

    def __str__(self):
        return "{} \n {}".format(Post.left, Post.right)


class Results(models.Model):
    result1 = models.FloatField()
    result2 = models.FloatField()

    def publish(self):
        self.save()

    def __str__(self):
        return "{} \n {}".format(Post.left, Post.right)
