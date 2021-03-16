from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['c_name']) < 5:
            errors['c_name'] = "The course name should be longer than 5 characters."
        if len(postData['desc']) < 10:
            errors['desc'] = "The course description is too short."
        return errors


class Course(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
