from peewee import *

db = SqliteDatabase('data/courses.db')

class BaseModel(Model):
    class Meta:
        database = db

class MajorCourses(BaseModel):
    course_name = CharField()
    major = CharField()

    # Can be used for calculating the distances between classes (might not needed as well)
    latitude = FloatField(null=True)
    longitude = FloatField(null=True)

    # There are more