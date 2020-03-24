# ask for n as an input then
# add all numbers from 1 to n.

while True: # setting output and input.
  output = ""
  num = int(input("enter a integer: "))

  if num == 0: # if num is 0 exit program.
    exit()

  for i in range(1, num+1):  # if the input integer is above 0 add all numbers
    output += "{}".format(i) # incrementing up to it as an integer.
    if i != num:
      output += "+"
  output += " = {}".format(sum(range(num+1))) # add the range whilst num+1
  print (output) # print the output
