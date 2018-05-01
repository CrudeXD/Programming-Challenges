x = input("Input a string to see if it's a palindrome: ")
back = ''

for i in range(len(x)):
  back = x[i] + back
if (back == x):
  print("It's a palindrome")
else:
    print("error 404")
