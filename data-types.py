# Lists in python

courses = ['History',".Maths",'English',"Physics","Chemistry"]
# print(courses)
# print('{} courses in the list'.format(len(courses)))
# print(courses[-1])
courses.append("Computer Science")
courses.insert(1,"Biology")
# print(courses)
# print(courses.index('Chemistry'))

# difference b/w append and extend
# append -> it will insert list into another list.
# extend -> will insert individual items into other list

# for index,course in enumerate(courses):
#     print(index+1,course)



# tuples in python

# tuples are Immutable where as lists are mutable. tuples are comparatively more faster than lists.

friends = ('Avinash','Rajesh','Manthan','Priyanshu')

# sets in python
# sets are un-ordered list and contains no duplicates.
cs_courses = {'Programming and data-structures','Computer Network','Operating System','DBMS','DBMS'}
cs_courses.add('Computer Architecture')
print(cs_courses)


# sets are optimized for the membership tests. gives much faster results.
# print("DBMS" in cs_courses)
# intersection() -> to find common elems in two sets
# difference() - to find different elems in two sets.
# union() -> to combine two sets.

# to create an empty sets , only can be done by
empty_set = set()