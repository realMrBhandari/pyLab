input_string = input("Input string to be aligned: ")
print(
    """Avilable shift methods: 
1. ljust
2. rjust
3. center 
"""
)
shift_type = input("Shift Method: ")
while shift_type not in ["1", "2", "3"]:
    print("Incorrect input! Try again")
    shift_type = input("Shift Method: ")
width_arg = input("Input string length: ")
while width_arg.isnumeric() == False:
    print("Input width argument is not an integer! Try again")
    width_arg = input("Input string length: ")
width_arg = int(width_arg)
char_arg = input("Input padding fill character: ") or " "
while len(char_arg) != 1:
    print("The fill character must be exactly one character long. Try again!")
    char_arg = input("Input padding fill character: ") or " "

new_string = None
if width_arg > len(input_string):
    if shift_type == "1":
        new_string = input_string + ((width_arg - len(input_string)) * char_arg)
    elif shift_type == "2":
        new_string = ((width_arg - len(input_string)) * char_arg) + input_string
    elif shift_type == "3":
        padding = width_arg - len(input_string)
        padding_half = padding // 2  # floar division
        new_string = (
            (char_arg * padding_half)
            + input_string
            + ((padding - padding_half) * char_arg)
        )
    print(new_string, len(new_string))
else:
    print(input_string, len(input_string))
