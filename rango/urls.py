# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:00:56 2020

@author: wexne
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns=[
        path('',views.index,name='index'),
        ]