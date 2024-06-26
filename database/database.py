import json
import os
import sys
cur_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path+"/..")

from datetime import datetime
from peewee import *
from models import Course, initialize_db

def parse_json(input):

    # if not Course.table_exists():
    #     db.create_tables([Course])

    with open(input, 'r') as file:
        data = json.load(file)

        classes = data
        for c in classes:
            gen_ed = ''
            for ge in c['generalEducation']:
                gen_ed += (ge['geCode'] + '/')
                gen_ed += (ge['geCollege'] + ',')

            classEnrollCode = None
            instructor = None
            days = None
            beginTime = None
            endTime = None

            if len(c['classSections']) != 0:
                classEnrollCode = c['classSections'][0]['enrollCode']

                if len(c['classSections'][0]['instructors']) != 0:
                    instructor = c['classSections'][0]['instructors'][0]['instructor']

                if len(c['classSections'][0]['timeLocations']) != 0:
                    days = c['classSections'][0]['timeLocations'][0]['days']
                    beginTime = c['classSections'][0]['timeLocations'][0]['beginTime']
                    endTime = c['classSections'][0]['timeLocations'][0]['endTime']
            
            course = Course(
                quarter = c['quarter'],
                courseId = c['courseId'],
                title = c['title'],
                contactHours = c['contactHours'],
                description = c['description'],
                college = c['college'],
                objLevelCode = c['objLevelCode'],
                subjectArea = c['subjectArea'], 
                unitsFixed = c['unitsFixed'], 
                unitsVariableHigh = c['unitsVariableHigh'], 
                unitsVariableLow = c['unitsVariableLow'], 
                delayedSectioning = c['delayedSectioning'], 
                inProgressCourse = c['inProgressCourse'], 
                gradingOption = c['gradingOption'], 
                instructionType = c['instructionType'], 
                onLineCourse = c['onLineCourse'], 
                deptCode = c['deptCode'], 
                generalEducation = gen_ed,
                classEnrollCode = classEnrollCode,
                days = days,
                beginTime = beginTime,
                endTime = endTime,
                instructor = instructor
            )

            try:
                course.save(force_insert=True)
            
            except Exception as e:
                print(f"An error occurred: {e}")

def get_all_courses():
    """
    Retrieves all courses from the database

    ARGS: 
        None

    RETURN:
        A list of Course instances
    """

    courses = []
    for c in Course.select():
        courses.append(c)
    
    return courses

def filter_by_unit(unit_low, unit_high, courses):
    """
    filter courses by a unit range. If want a specific unit, pass the same value
    for unit_low and unit_high

    ARGS:
        unit_low: (int) # units lower range
        unit_high: (int) # units higher range
        courses: (list) list of Courses instances

    RETURN:
        A list of Course instances that match the conditions
    """

    filtered_courses = []
    for c in courses:
        if c.unitsFixed is not None:
            if unit_low <= c.unitsFixed <= unit_high:
                filtered_courses.append(c)
    
    return filtered_courses

def filter_by_ge(college, area, courses):
    """
    filter courses by ge area

    ARGS:
        college: (str) collge
        area: (str) area
        courses: (list) list of Courses instances

    RETURN:
        A list of Course instances that match the conditions
    """
    filtered_courses = []
    for c in courses:
        if c.generalEducation is not None:
            if college in c.generalEducation and area in c.generalEducation:
                filtered_courses.append(c)
    
    return filtered_courses

def filter_by_time(day, begin, end, courses):
    """
    filter courses by time

    ARGS:
        day: (str) day of the week. One letter
        begin: (str) begin time HH:MM
        end: (str) end time in formate HH:MM
        courses: (list) list of Courses instances

    RETURN:
        A list of Course instances that match the conditions
    """

    def is_time_range_within(course_begin, course_end, available_begin, available_end):
        course_begin = datetime.strptime(course_begin, "%H:%M").time()
        course_end = datetime.strptime(course_end, "%H:%M").time()
        available_begin = datetime.strptime(available_begin, "%H:%M").time()
        available_end = datetime.strptime(available_end, "%H:%M").time()

        return available_begin <= course_begin and course_end <= available_end

    filtered_courses = []

    for c in courses:
        if c.days is not None and day.upper() not in c.days:
            continue
        if c.beginTime is not None and c.endTime is not None:
            if is_time_range_within(c.beginTime, c.endTime, begin, end):
                filtered_courses.append(c)

    return filtered_courses

if __name__ == "__main__":
    initialize_db()
    parse_json('api_responses.json')
    temp = get_all_courses()
    for i in temp:
        print(f"{i.courseId}, {i.beginTime}, {i.endTime}")

    print("\nfiltered by time\n")

    temp = filter_by_time("M", "11:00", "15:00", temp)
    for i in temp:
        print(f"{i.courseId}")