import json
from peewee import *
from datetime import datetime

# db = SqliteDatabase('data/courses.db')

# class BaseModel(Model):
#     class Meta:
#         database = db

# class MajorCourses(BaseModel):
#     course_name = CharField()
#     major = CharField()

#     # Can be used for calculating the distances between classes (might not needed as well)
#     latitude = FloatField(null=True)
#     longitude = FloatField(null=True)

#     # There are more

"""
File: database.py
Description: Parse json file and store in the database. Course filter methods.
"""

db = SqliteDatabase('data/courses.db')

class Course(Model):
    quarter = CharField()
    courseId = CharField()
    title = CharField()
    contactHours = FloatField(null=True)
    description = CharField(null=True)
    college = CharField(null=True)
    objLevelCode = CharField(null=True)
    subjectArea = CharField(null=True)
    unitsFixed = FloatField(null=True)
    unitsVariableHigh = FloatField(null=True)
    unitsVariableLow = FloatField(null=True)
    delayedSectioning = CharField(null=True)
    inProgressCourse = CharField(null=True)
    gradingOption = CharField(null=True)
    instructionType = CharField(null=True)
    onLineCourse = BooleanField(null=True)
    deptCode = CharField(null=True)
    generalEducation = CharField(null=True)
    classEnrollCode = CharField(null=True)
    days = CharField(null=True)
    beginTime = CharField(null=True)
    endTime = CharField(null=True)
    instructor = CharField(null=True)

    class Meta:
        primary_key = CompositeKey('quarter', 'courseId', 'classEnrollCode')
        database = db


def initialize_db():
    db.connect()
    db.create_tables([Course], safe=True)