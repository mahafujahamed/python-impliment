command = ""
while True:
    command = input(">> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car is Stopped...")
    elif command == "help":
        print("""
              start - to start the car
              stop - to stop the car
              quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")