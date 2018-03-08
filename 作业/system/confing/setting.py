import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADMIN_DB = os.path.join(BASEDIR, 'db', 'admin')
COURSE_DB = os.path.join(BASEDIR, 'db', 'course')
CLASSES_DB = os.path.join(BASEDIR, 'db', 'classes')
STUDENT_DB = os.path.join(BASEDIR, 'db', 'student')
TEACHER_DB = os.path.join(BASEDIR, 'db', 'teacher')
SCHOOL_DB = os.path.join(BASEDIR, 'db', 'school')