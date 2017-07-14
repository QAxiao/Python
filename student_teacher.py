#!/usr/bin/env python3

from collections import Counter
from collections import defaultdict
import sys

class Person(object):
    """
    è¿åå·æç»å®åç§°ç Person å¯¹è±¡
    """

    def __init__(self, name,grade = None):
        self.name = name
        self.grade = grade

    def get_details(self):
        """
        è¿ååå«äººåçå­ç¬¦ä¸²
        """
        return self.name
    
    def get_grade(self):
        return self.grade


class Student(Person):
    """
    è¿å Student å¯¹è±¡ï¼éç¨ name, branch, year 3 ä¸ªåæ°
    """

    def __init__(self, name, branch, year, grade = None):
        Person.__init__(self, name, grade=None)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        è¿ååå«å­¦çå·ä½ä¿¡æ¯çå­ç¬¦ä¸²
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)
    
    def get_grade(grade):
        res = Counter(grade)
        fail = 0
        Pass = 0
        for k in list(res.elements()):
            if k =="D":
                fail +=1
            else:
                Pass +=1
        print("Pass: {}, Fail: {}".format(Pass,fail))

class Teacher(Person):
    """
    è¿å Teacher å¯¹è±¡ï¼éç¨å­ç¬¦ä¸²åè¡¨ä½ä¸ºåæ°
    """
    def __init__(self, name, papers, grade=None):
        Person.__init__(self, name, grade = None)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(grade):
        res = Counter(grade)
        g = []
        for k in res.most_common(len(res)):
            g.append("{}: {}".format(k[0],k[1]))
        print(", ".join(g))

person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

#print(person1.get_details())
#print(student1.get_details())
#print(teacher1.get_details())

if __name__ == "__main__":
    if sys.argv[1] == "teacher":
        Teacher.get_grade(sys.argv[2])
    elif sys.argv[1] == "student":
        Student.get_grade(sys.argv[2])
    else:
        sys.exit(0)
