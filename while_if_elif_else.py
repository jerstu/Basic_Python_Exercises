prompt = ""
started = False
while True:
    prompt = input("> ").lower()
    if prompt == "help":
        print("start - to start the car"
              "\nstop - to stop the car"
              "\nquit to exit")
    elif prompt == "start":
        if started:
            print("Car is already started.")
        else:
            print("Car started...Ready to go!")
            started = True
    elif prompt == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            print("Car stopped.")
            started = False
    elif prompt == "quit":
        break
    else:
        print("I don't understand that...")