# food = input("Enter food you like (q to quit): ")

# # while food == "q":
# #     break
# # while food != "q":
# #     print(f"You like {food}")
# #     food = input("Enter another food you like (q to quit): ")

# # print("You have quit the loop")

# while food != "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")
# print("You have quit the while loop")


num = int(input("Enter a number between 1 and 10: "))

while num not in range(1,11):
    print("Enter valid number: ")
    num = int(input("Enter a number between 1 and 10: "))

print(f"{num}")
