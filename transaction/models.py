from django.db import models
from django.utils import timezone


class TransactionItem(models.Model):
    amount = models.PositiveIntegerField()
    due_date = models.DateField(default=timezone.now)
