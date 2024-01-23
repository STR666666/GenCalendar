import sqlite3

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "courses.db")

# sqliteConnection = sqlite3.connect('courses.db')
# sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
# cursor = sqliteConnection.cursor()
# cursor.execute(sql_query)
# print("List of tables\n")
# print(cursor.fetchall())

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect(db_path)

# Create a cursor object to interact with the database
cursor = conn.cursor()

#CENICEROS 



def get_courses_l2(cursor, selected_attributes = None, instructors= None, ge_area= None, ge_college = None,  available_begin= None, available_end= None, major_area = None): 

    #selected_columns = ["A", "B"]

    if selected_attributes is not None:
        sql_statment = f"SELECT {', '.join(selected_attributes)} FROM course\n"
    else:
        sql_statment = "SELECT * FROM course\n"


    if instructors is not None:
        instructors_str = ', '.join([f"'{instructor}'" for instructor in instructors])
        sql_statment += f"WHERE instructor IN ({instructors_str})\n AND "
    else : 
        sql_statment += f"WHERE\n"


    if ge_area is not None and ge_college is not None:
        if len(ge_area) == 1:
            #needs 2 spaces for some reason ?
            ge_str = ge_area + "  /" + ge_college
        else :
            ge_str = ge_area + "/" + ge_college
        sql_statment += f" generalEducation LIKE '%{ge_str}%'\n AND "
    
    
    if available_begin is not None and available_end is not None:
        sql_statment += f"' {available_begin}' <= beginTime And endTime <= '{available_end}'\n AND "
    
    if major_area is not None:
        sql_statment += f" deptCode like '{major_area}'\n AND "

    if sql_statment.endswith("AND "):
        sql_statment = sql_statment[:-5]

    print(sql_statment)
    cursor.execute(sql_statment)
    print(cursor.fetchall())

#get_courses_l2(cursor, selected_attributes=None, instructors=["STRATHMAN B A"])
#get_courses_l2(cursor, selected_attributes=None, ge_area="WRT", ge_college = "L&S")
#get_courses_l2(cursor, selected_attributes=None, ge_area="D", ge_college = "L&S")
#get_courses_l2(cursor, selected_attributes=None, available_begin= "08:00", available_end= "10:00")
#get_courses_l2(cursor, selected_attributes=None, major_area = "STATS")
#get_courses_l2(cursor, selected_attributes=None, instructors=["DONELAN J H"], available_begin= "08:00", available_end= "10:00")
