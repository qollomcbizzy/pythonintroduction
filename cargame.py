command = ""
started = False
stopped = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        # check if the car already started
        if started:
            print("Car has been started")
        else:
            started = True
            print("car started ...")
    elif command == "stop":
        # check if the car has been stopped
        if stopped:
            print('car has been stopped')
        else:
            stopped = True
            print("car stopped")
    elif command == "help":
        # multiline print
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Oops Sorry Check you Command")