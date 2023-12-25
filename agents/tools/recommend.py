import pandas as pd

class Course:
    def __init__(self, name = 0, day = 0, start = 0, end = 0, professor = 0, section = [], major = [], area = []):
        self.name = name
        self.day = day
        self.start = start
        self.end = end
        self.professor = professor
        self.section = section
        self.major = major
        self.area = area

    def setSection(self, section):
        self.section = section
    
    def printSection(self):
        i = 1
        for x in self.section:
            print(f"Section{i}: {x.day} {x.start}-{x.end}")
            i += 1

    def printInfo(self):
        print(self.name, self.day, f"{self.start}-{self.end}", self.professor, self.major, self.area)
        self.printSection()

def printCourseList(List):
    print("------------")
    for x in List:
        x.printInfo()
        print("------------")


df = pd.read_excel("Courses.xlsx", sheet_name = "Sheet2")


courseList = []
sectionList = []
courseNum = len(df["Name"])
i = 0
while i < courseNum:
    name = df["Name"].loc[df.index[i]]
    day = df["Day"].loc[df.index[i]]
    start = float(df["Start"].loc[df.index[i]])
    end = float(df["End"].loc[df.index[i]])
    professor = df["professor"].loc[df.index[i]]
    if (name == "Section"):
        target = Course(name, day, start, end, professor)
        sectionList.append(target)
        if (i == courseNum - 1):
            courseList[-1].setSection(sectionList)
    else:
        if (i > 0):
            courseList[-1].setSection(sectionList)
        major = str(df["major"].loc[df.index[i]]).split(", ")
        area = str(df["area"].loc[df.index[i]]).split(", ")
        target = Course(name, day, start, end, professor, [], major, area)
        courseList.append(target)
        sectionList = []
    i += 1

# printCourseList(courseList)

timeConstS = float(input("Enter your time constraint begin: "))
timeConstF = float(input("Enter your time constraint finish: "))
profConst = []
while True:
    profN = input("Enter the professor you like very much: ")
    if profN == "":
        break
    profConst.append(profN)
majorConst = []
while True:
    majorN = input("Enter the major you want to take: ")
    if majorN == "":
        break
    majorConst.append(majorN)
areaConst = []
while True:
    areaN = input("Enter the GE area you want to take: ")
    if areaN == "":
        break
    areaConst.append(areaN)

resultList = []
for course in courseList:
    if (course.professor in profConst):
        resultList.append(course)
        continue
    if (not (course.end <= timeConstS or course.start >= timeConstF)):
        continue
    if (majorConst != [] and not (course.major in majorConst)):
        continue
    if (areaConst != [] and not (course.area in areaConst)):
        continue
    resultList.append(course)


printCourseList(resultList)