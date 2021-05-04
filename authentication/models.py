# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.models import User

from django.db import models
from django.urls import reverse
from datetime import datetime   



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, default='BAN' )
    team = models.CharField(max_length=30, default='EBB')
    group = models.CharField(max_length=30,default='EBB' )
    phonenumber = models.CharField(max_length=30, default='0000000000' )

    def __str__(self):
        return self.user.username

class HardWareForm_table(models.Model):
    AssetNo          = models.CharField(max_length=50)
    Owner            = models.CharField(max_length=50)
    AssetTypeModel   = models.CharField(max_length=50)
    Group            = models.CharField(max_length=50)
    TeamName         = models.CharField(max_length=50)
    ProductLine      = models.CharField(max_length=50)
    Remark           = models.CharField(max_length=400)

    def __str__(self):
        return self.AssetNo



class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    start_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    end_time = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('authentication:event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        print("get_html_url")
        print(self.id)
        url = reverse('event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.user)









