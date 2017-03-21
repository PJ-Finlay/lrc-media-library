from __future__ import unicode_literals
import datetime
from django.db import models
import re

class Media(models.Model):
    title = models.CharField(max_length=100)

    #Media Server Url ex. mov3.mp4
    url = models.CharField(max_length=100)

    #This needs to be entered exactly to group by language
    language = models.CharField(max_length=100)

    #Course Name ex CS 1110
    #Comma seperated if multiple courses ex. cs1110, cs2110
    course_name = models.CharField(max_length=100)

    verified_working = models.BooleanField(default=True)

    #This will be displayed to users viewing the media file
    additional_information = models.CharField(max_length=1000, blank=True)

    enable_subtitles = models.BooleanField(default=True)

    #If the code needs to be entered to access the course
    require_access_code = models.BooleanField(default=True)

    #If the media file should only be allowed to be viewed in the timeframe given below
    restrict_to_timeframe = models.BooleanField(default=False)

    #Start availability
    start_date = models.DateField(default=datetime.date.today)

    #End availability
    end_date = models.DateField(default=datetime.date.today)

    #The day the media was dropped off
    drop_off_date = models.DateField(default=datetime.date.today)

    requested_by = models.CharField(max_length=100, blank=True)

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

    #Format (DVD/VHS/Digital)

    DIGITAL = 'i'
    DVD = 'd'
    VHS = 'v'
    FORMAT_CHOICES = (
        (DIGITAL,'Library'),
        (DVD,'Personal'),
        (VHS,'Department'),
    )
    format = models.CharField(
        max_length=1,
        choices=FORMAT_CHOICES,
        default=DIGITAL,
    )

    #Notes
    notes = models.CharField(max_length=1000, blank=True)

    #Returns true if no code is required or if a valid code is supplied
    def is_valid_code(self, code):
        if not self.require_code:
            return True

        code = code.strip()

        course_names = self.course_name.split(',')

        for course_name in course_names:
            #Get course number ex. CS1110 -> 1110
            match = re.findall(r'[0-9]+', course_name)
            if len(match) == 1:
                course_number = match[0]
            else:
                course_number = ''

            correct_code = self.language.lower().strip() + course_number # ex. french1110

            if correct_code == code:
                return True

        return False
