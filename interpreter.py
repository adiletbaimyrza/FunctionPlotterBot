import re

#Create an Input class to handle user input
class Input:

    # Define a method to take user input and return it as a string
    def take_input() -> str:
        eq = input("type your equation: ")
        return eq

    # Define a method to check if a linear equation matches a certain pattern
    def check_pattern_linear(text):
        # Define the regular expression pattern to match the linear equation
        pattern = re.compile("^f\(x\)\s*=\s*(-)?\s*(\d*(\.\d*)?)?(x)?\s*([+-])?\s*(\d*(\.\d*)?)?$")
        # Search for the pattern in the text
        mt = pattern.search(text)

        # Extract the matched groups
        args = []

        for _ in range(1,8):
            args.append(mt.group(_))

        # Print the extracted arguments for debugging purposes
        print(args)

        return args

    # Define a method to extract the coefficients of a linear equation from its arguments
    def extract_args(args) -> list:
        # Check if the equation is of the form ax + c = 0
        if args[3] == None and args[4] == None and args[5] == '' and args[6] == None:
            c = -1*float(args[1]) if args[0] == '-' else float(args[1])
            a = 0
            # Check if the equation is of the form ax = c
        elif args[4] == None and args[5] == '':
            a = -1*float(args[1]) if args[0] == '-' else float(args[1])
            c = 0
            # Otherwise, the equation is of the form ax + c = d
        else:
            a = -1*float(args[1]) if args[0] == '-' else float(args[1])
            c = -1*float(args[5]) if args[4] == '-' else float(args[5])

        return [a, c]
        
        
        
        
    

        

