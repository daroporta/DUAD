
class Parameter():
    def __init__(self, *args):
        self.args=args
        
        
def decorator(func):
    def check_if_number(arg, *args):
        try:
            for arg.args in arg.args:
                if isinstance(arg.args, (int, float)):
                    func(arg)
                else:
                    try:
                        number=int(arg.args)
                        func(arg)
                    except:
                        number=float(arg.args)
                        func(arg)
        except:
            print(f"The parameter {arg.args} is not a number.")

    return check_if_number


@decorator
def determine_if_number(arg):
    print(f"The parameter {arg.args} is a number")


numbers=Parameter("34", 55, 85.2, "99.5", "hi")

determine_if_number(numbers)
