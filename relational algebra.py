"""
http://faculty.ung.edu/zmiller/4022K/hws/Relational_Algebra.html
"""

people = set([('Lindsay', 16, 'female'),
              ('Tom', 21, 'male'),
              ('Eric', 33, 'male'),
              ('Marco', 13, 'male'),
              ('Kristopher', 45, 'male'),
              ('Kelly', 21,     'female'),
              ('Mitchell', 24, 'male'),
              ('Tammy', 30, 'female'),
              ('Brad', 18, 'male '),
             ])

#Implementing Relational Algebra Operators - Set operations¶
other_people = set([('Lindsay', 16, 'female'),
                    ('Tom', 21, 'male'),
                    ('Eric', 33, 'male'),
                    ('Marco', 13, 'male'),
                    ('Daniel', 36, 'male'),
                   ])
"""print("people.intersection(other_people), kesişen")
print(people.intersection(other_people))"""
"""print("people.union(other_people), hepsi")
print(people.union(other_people), )"""
"""print("people - other_people, peopleda olup other_people da olmayan")
print(people - other_people)
print("other_people - people, other_people da olup da ötekinde olmayan")
print(other_people - people)"""

#Implementing Relational Algebra Operators - Selection¶
under_22 = []
for rider in people:
    if rider[1] < 22:
        under_22.append(rider)

# Implementing Relational Algebra Operators - Cross Product¶

def crossproduct(a, b):
    newrelation = []
    for row in a:
        for r in b:
            newrelation.append(tuple([item for item in row] + [item for item in r]))
    return set(newrelation)
result = crossproduct(people, bike)
names = set([row for row in crossproduct(people, bike) if row[0] == row[3] and row[4] == 'Honda'])


# Implementing Relational Algebra Operators - Derived Operators
names = set([row for row in crossproduct(people, bike) if row[0] == row[3] and row[4] == 'Honda'])


# Implementing Relational Algebra Operators - Project¶
from collections import namedtuple
Person = namedtuple('Person', 'name age gender')
people = set([Person('Lindsay', 16, 'female'),
              Person('Tom', 21, 'male'),
              Person('Eric', 33, 'male'),
              Person('Marco', 13, 'male'),
              Person('Kristopher', 45, 'male'),
              Person('Kelly', 21,       'female'),
              Person('Mitchell', 24, 'male'),
              Person('Tammy', 30, 'female'),
              Person('Brad', 18, 'male '),
             ])

def project(relation, columns):
    """Relational algebra project operator

    >>> from collections import namedtuple
    >>> Person = namedtuple('Person', 'name age gender')
    >>> people = set([Person('Lindsay', 16, 'female'),
         Person('Tom', 21, 'male'), Person('Eric', 33, 'male')])
    >>> project(people, 'name')
    set([('Lindsay',), ('Tom',), ('Eric',)])

    """
    return set([tuple(getattr(row, column) for column in columns.split())
                for row in relation])

print(project(people, 'name'))

