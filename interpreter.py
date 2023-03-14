import re


class Input:

    def take_input() -> str:
        eq = input("type your equation: ")
        return eq

    def check_pattern_linear(text):
        pattern = re.compile("^f\(x\)\s*=\s*(-)?\s*(\d*(\.\d*)?)?(x)?\s*([+-])?\s*(\d*(\.\d*)?)?$")
        mt = pattern.search(text)

        args = []

        for _ in range(1,8):
            args.append(mt.group(_))
        

        print(args)

        return args
    
    def extract_args(args) -> list:
        if args[3] == None and args[4] == None and args[5] == '' and args[6] == None:
            c = -1*float(args[1]) if args[0] == '-' else float(args[1])
            a = 0
        elif args[4] == None and args[5] == '':
            a = -1*float(args[1]) if args[0] == '-' else float(args[1])
            c = 0
        else:
            a = -1*float(args[1]) if args[0] == '-' else float(args[1])
            c = -1*float(args[5]) if args[4] == '-' else float(args[5])

        return [a, c]
        
        
        
        
    

        

