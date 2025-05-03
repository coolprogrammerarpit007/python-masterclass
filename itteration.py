# for number in [1,2,3,4,5,6,7,8,9,10]:
#     if number%2 == 0:
#         continue
#     if number == 7:
#         break
#     print(f"Number: {number}")


friends = ('RAJESH','Avinash','Gaurav','Priyanshu','Pranshu')

def greet_friend(friends):
    for friend in friends:
        print(f"Nice to meet you {friend}")

# greet_friend(friends)


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)


courses = ['Physics','Chemistry','Maths']
student_data = {'name':'leon','age':25}
student_info(*courses,**student_data)