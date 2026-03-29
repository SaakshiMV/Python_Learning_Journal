import sys
from converter import convert_currency

def show_help():
    print("""
Usage:
python main.py convert <amount> <from_currency> <to_currency>
""")

if len(sys.argv) != 5:
    show_help()
else:
    command = sys.argv[1]

    if command == "convert":
        try:
            amount = float(sys.argv[2])
            base = sys.argv[3].upper()
            target = sys.argv[4].upper()

            result = convert_currency(amount, base, target)

            if result is not None:
                print(f"{amount} {base} = {result} {target}")

        except ValueError:
            print("Amount must be a number!")

    else:
        print("Unknown command!")
        show_help()
