# Control Structures - While Loop

"""

- The program continually asks the user to enter a number

- When the user enters -1 the programme stops asking the user to enter a number

- The program then calculate the avg of the numbers entered, excluding the -1

- Test user inputs

- Account for any non digit entries and add relevant error message

- Account for user entries that are negative numbers and floats

"""
# place holders for total/count and user input

input_total = 0
input_count = 0
user_number = 0
user_list = []

while user_number != -1:
    try:
        user_number = input("Please enter a number, (Enter -1 to stop): ")

        # casting user_number to a float
        user_number = float(user_number)

        # step accounting for user entering -1 to start off with (exit)
        if user_number == -1 and input_count == 0:
            print(f"You are exiting the program.")
            break

        # adding count and total for any number that is not a -1
        elif user_number != -1:
            input_total += user_number
            user_list += [user_number]
            input_count += 1
            continue

    except ValueError or TypeError:
        error_message = f"You entered: {user_number}. This is invalid"
        print(error_message)
        continue

    # printed output rounded up to 2 decimal place
    else:
        avg = input_total / input_count

        print(f"The numbers you have entered are: {user_list}")
        print(f"The total is: {input_total:,.2f}")
        print(f"The count is: {input_count:,.2f}")
        print(f"The average is: {avg:,.2f}")
        break
