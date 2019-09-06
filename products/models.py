from django.db import models

# Create your models here.

class Listing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rate_of_interest = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name, self.rate_of_interest)

    def __unicode__(self):
        return "{} {}".format(self.name, self.rate_of_interest)

class Coverage(models.Model):
    product = models.ForeignKey(Listing, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name, self.product)

    def __unicode__(self):
        return "{} {}".format(self.name, self.product)

    # COMPLETE THIS TASK BEFORE GOING TO THE OTHER LOAN APPLICATION
