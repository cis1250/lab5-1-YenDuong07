#!/usr/bin/env python3

def validating(user_input):
  while True:
    user_input = input("Enter a number: ")
    user_input = int(user_input)
    if user_input >= 0:
      break
    else:
      print("try again")
  return user_input

def fibonacci(user_input):
  if user_input == 0:
    print(0)
  elif user_input ==1:
    print(0)
    print(1)
  else:
    f_zero = 0
    f_one = 1
    print(f_zero)
    print(f_one)
    for x in range (2, user_input):
      answer = f_zero + f_one
      print_fib(answer)
      f_zero = f_one
      f_one = answer

def print_fib (answer):
  print(answer)

user_input = validating(user_input)
fibonacci(user_input)

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
