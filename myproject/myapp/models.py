# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=20)
    body= models.TextField();
    created_at = models.DateTimeField(default=datetime.now,blank=True )