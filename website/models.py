from __future__ import unicode_literals
import datetime
from django.db import models
import re

class Media(models.Model):
    #The user facing name of the media file
    title = models.CharField(max_length=100)

    #Media Server Url ex. mov3.mp4
    url = models.CharField(max_length=100)

    #This needs to be entered exactly to group by language
    language = models.CharField(max_length=100)

    #Notes
    notes = models.CharField(max_length=1000, blank=True)

    #Course Name ex CS 1110
    course_name = models.CharField(max_length=100)

    #If the code needs to be entered to access the course
    require_code = models.BooleanField(default=True)

    #If the media file should only be allowed to be viewed in the timeframe given below
    restrict_to_timeframe = models.BooleanField()

    #Start availability
    start_date = models.DateField(default=datetime.date.today)

    #End availability
    end_date = models.DateField(default=datetime.date.today)

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

    #Returns true if no code is required or if a valid code is supplied
    def is_valid_code(self, code):
        if not self.require_code:
            return True

        code = code.strip()

        #Get course number ex. CS1110 -> 1110
        match = re.findall(r'[0-9]+', self.course_name)
        if len(match) == 1:
            course_number = match[0]
        else:
            course_number = ''

        correct_code = self.language.lower().strip() + course_number # ex. french1110

        if correct_code == code:
            return True

        return False
