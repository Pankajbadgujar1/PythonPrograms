a = 10
print(a)

# This is an example of how to print in python
#Practical examples of python programmming :
# 1 control structure
#Loops 
#for loop
print('This is control structrue example of for loop  ')
print('Enter a string and check how many whovels present in string ')
c = 0
str = input("Enter a string : ")
for ch in str:
    if ch in 'aeiouAEIOU':
        c+=1
print(f'In the above string {c} no of vovels presents...')
