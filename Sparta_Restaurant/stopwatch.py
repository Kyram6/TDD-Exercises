import time

print(time.time()) #unix time
# seconds since jan 1 1970

print(time.ctime()) #ctime = current time

#write a function that will calc how long it takes to multiply 2 numbers

# def multiply_time(a, b):
#     start_time = time.time()
#
#     result = a * b
#
#     end_time = time.time()
#
#     print(f"the answer is {result} - this took {end_time - start_time} seconds. ")
#
# multiply_time(10,20)
#
#
# print("pausing for 5 seconds..")
# time.sleep(5)
# print("pause completed")

# name = input("whats your name?")
# print(f"Hello,{name}!")
#
# ask_again = True
# while ask_again:
#     proceed = input("Do you want to proceed? Y/N\n>").upper()
#     if proceed == "Y":
#         print("proceeding...")
#         ask_again = False
#     elif proceed == "N":
#         print("stopping")
#         ask_again = False

# Build a Python Stopwatch!  Enter to start, enter to stop, how long has elapsed!

# Hint: KeyboardInterrupt is something that can be picked up with a try/except block.

input("Press Enter to start stopwatch..")
start_time = time.time()
last_lap_time = start_time
lap_number = 1

print("Stopwatch started")

while True:
    action = input("Type 'lap' to record a lap or 'stop' to finish...")

    if action == "lap":
        current_time = time.time()

        lap_time = current_time - last_lap_time
        total_time = current_time - start_time

        print(f" Lap {lap_number}")
        print(f" Lap Time:{lap_time:.3f} seconds")
        print(f" Total Time: {total_time:.3f} seconds")

        last_lap_time = current_time
        lap_number +=1

    elif action == "stop":
        end_time = time.time()
        total_time = end_time - start_time

        print(f"Timer Stopped")
        print(f"Final time: {total_time:.3f} seconds")

        break





#   Or a log of previous times? 


