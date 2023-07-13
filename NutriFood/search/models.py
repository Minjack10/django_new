from django.db import models


class produit(models.Model):
    produit_text = models.CharField(max_length=200)
    ingredient_text = models.CharField(max_length=200)


