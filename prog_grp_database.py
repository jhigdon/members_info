"""
started by Albert Sun, 11/20/2016
this is a simple program to obtain and store data about members of the Wilkes Barre Programming Group
using Python 3.5

currently writing list as a JSON txt file.  would like to implement as SQL or use Pandas to analyze
- future implementation?
"""
import json
import peewee

database = peewee.SqliteDatabase("members.db")

class Member(peewee.Model):
    """
    model of WB programming members with skills and interests
    """
    name = peewee.CharField()

    class Meta:
        database = database
        
class Skills(peewee.Model):
    member = peewee.ForeignKeyField(Member, related_name="skills")
    skill = peewee.CharField()

    class Meta:
        database = database

class Interests(peewee.Model):
    member = peewee.ForeignKeyField(Member, related_name="interests")
    interest = peewee.CharField()

    class Meta:
        database = database

def read_in(file):
    try :
        with open(file, 'r') as f:
            return json.load(f)
    except :
        return []

def write_out(userdata, file):
    with open(file, 'w') as f:
        json.dump(userdata, f)

#print (read_in("member_dat.txt"))

# moo = read_in("member_dat.txt")


if __name__ == "__main__":
    try:
        Member.create_table()
        database.create_tables([Member, Skills, Interests], safe=True)
    except peewee.OperationalError:
        print("some table table already exists lol")

    #member = Member.create(name="Jonathan")
    # Skills.create(member=member, skill="Lisp")
    # Skills.create(member=member, skill="Emacs")

