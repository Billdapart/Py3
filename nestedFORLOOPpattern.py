# Write a Python program to construct the following pattern, using a nested for loop.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

num=5;
for star in range(num):
    for repeat in range(star):
        print ('* ', end="")
    print('')

for star in range(num,0,-1):
  for repeat in range(star):
    print('* ', end="")

  print('')
