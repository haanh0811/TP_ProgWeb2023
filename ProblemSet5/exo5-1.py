
from django.db import models
from blog.models import Blog, Entry
# 1
"""CREATE TABLE classrooms(
id INTEGER PRIMARY KEY AUTOINCREMENT,
roomname TEXT NOT NULL,
seats INTEGER DEFAULT 50 NOT NULL
)"""

class Classrooms(models.Model):
    roomname = models.CharField()
    seats = models.IntegerField(default=50)

#2
"""The SQL statements below fills the table “classrooms” with some rows of data.
How would this be achieved in Django?"""

#INSERT INTO classrooms (roomname, seats) VALUES ('A101', 42);

class1 = Classrooms(roomname='A101',seats= 42)
class1.save()

#INSERT INTO classrooms (roomname) VALUES ('A102');
class2 = Classrooms(roomname='A102')
class2.save()

#3
"""The SQL statements below retrieves data from the classrooms table. How would
this be achieved in Django?"""
#SELECT * FROM classrooms WHERE seats > 45;

Entry.objects.all().filter(seats__gt = 45)