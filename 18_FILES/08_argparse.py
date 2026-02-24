import argparse

parser = argparse.ArgumentParser(description="simple_Calculator")
parser.add_argument("num1", type=float, help="firse_number")
parser.add_argument("num2", type=float, help="second_number")
parser.add_argument("operation", choices=["add", "sub", "mult", "div"], help="Operation to perform")

args = parser.parse_args()

if(args.operation == "add"):
    print(f"The result is {args.num1 + args.num2}")

elif(args.operation == "sub"):
    print(f"The result is {args.num1 - args.num2}")

elif(args.operation == "mult"):
    print(f"The result is {args.num1 * args.num2}")

elif(args.operation == "div"):
    print(f"The result is {args.num1 / args.num2}")

else:
    print("Error")
    
    
    