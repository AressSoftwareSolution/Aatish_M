# Loop is way that repeat a block of code multiple time without writing it again and again 
# for loop repeats a block of code for a specific number of times
# while loop repeats a block of code as long as the conditin is true

# For loop:
name = "Hello"
count=0
for i in name:
    if(i=="l"):
        count = count + 1
print(count)

colors =["Red","Orange","Pink","White"]
for i in colors:
    print(i)
    for j in i:
        print(j)

#  using range 
for i in range(1,11):
    print(i)


#While loop: 
i=0
while(i<5):
    print(i)
    i=i+1
print("Done !!!!")
