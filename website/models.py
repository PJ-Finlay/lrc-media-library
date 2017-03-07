from __future__ import unicode_literals

from django.db import models

class Media(models.Model):
    #The user facing name of the media file
    title = models.CharField(max_length=100)

    #Media Server Url ex. mov3.mp4
    url = models.CharField(max_length=100)

    #Notes
    notes = models.CharField(max_length=1000)

    #Course Name ex CS 1110
    course_name = models.CharField(max_length=100)

    #If the media file should only be allowed to be viewed in the timeframe given below
    restrict_to_timeframe = models.BooleanField()

    #Start availability
    start_date = models.DateField()

    #End availability
    end_date = models.DateField()

    #Ownership (Personal/Department/Library)
    PERSONAL = 'p'
    DEPARTMENT = 'd'
    LIBRARY = 'l'
    OWNERSHIP_CHOICES = (
        (PERSONAL,'Personal'),
        (DEPARTMENT,'Department'),
        (LIBRARY,'Library'),
    )
    ownership = models.CharField(
        max_length=1,
        choices=OWNERSHIP_CHOICES,
        default=PERSONAL,
    )
