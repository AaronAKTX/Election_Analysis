x = 8
if x==1:
    print('x is equal to 1')
elif x < 10:
    print('x is less than 10')
else:
    print('x is greater than 1')
    
is_nice = False
state ="nice" if is_nice else "not nice"
print("The cat is ", state)
name = "Dan"
group_one = ["greg","Tony","Susan"]
group_two = ["Gerald","Paul","Gerry"]
group_three = ["Carla","Dan","Jefferson"]

for person in group_two:
    print(person)
    print("au" in person)

for l in range(0,10,2):
    print(l)