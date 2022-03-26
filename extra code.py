if response is no:
    print("Thank you for playing!")
    quit()
if response is yes:
    print(fortunes)
for fortunes in fortune_file:
    again = input("Would you like another fortune?")
    if again is no:
        print("Thank you for playing!")
        quit()
    if again is yes:
        print(fortunes)