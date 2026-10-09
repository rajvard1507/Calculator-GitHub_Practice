import math

import operations
import history


# Display the calculator menu

def display_menu():
    print("\n" + "=" * 45)
    print("          ADVANCED SCIENTIFIC CALCULATOR")
    print("=" * 45)

    print("\nBASIC OPERATIONS")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    print("\nPOWERS AND ROOTS")
    print("5. Square")
    print("6. Cube")
    print("7. Square Root")
    print("8. Cube Root")
    print("9. Power (x^y)")
    print("10. Reciprocal (1/x)")

    print("\nSCIENTIFIC OPERATIONS")
    print("11. Exponential (e^x)")
    print("12. Natural Logarithm (ln)")
    print("13. Logarithm Base 10")
    print("14. Sine (sin)")
    print("15. Cosine (cos)")
    print("16. Tangent (tan)")
    print("17. Factorial")
    print("18. Percentage")

    print("\nHISTORY")
    print("19. View History")
    print("20. Clear History")
    print("21. Delete History Entry")

    print("\n0. Exit")
    print("=" * 45)


# Read a valid number

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))

            if not math.isfinite(number):
                print("Please enter a finite number.")
                continue

            return number

        except ValueError:
            print("Invalid input. Please enter a number.")


# Format results for display

def format_result(result):
    if isinstance(result, float):
        if not math.isfinite(result):
            raise ValueError("The result is outside the supported numeric range.")

        if result == 0:
            return "0"

        if result.is_integer():
            return str(int(result))

        return f"{result:.12g}"

    return str(result)


# Perform a calculation and save it

def calculate(operation, expression, *numbers):
    result = operation(*numbers)
    formatted_result = format_result(result)

    print(f"\nResult: {formatted_result}")

    history.add_history(expression, formatted_result)


# Main application

def main():
    print("\nWelcome to the Advanced Scientific Calculator!")

    while True:
        display_menu()

        choice = input("\nEnter your choice: ").strip()

        try:

            # Basic arithmetic

            if choice == "1":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                calculate(operations.add, f"{a} + {b}", a, b)

            elif choice == "2":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                calculate(operations.subtract, f"{a} - {b}", a, b)

            elif choice == "3":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                calculate(operations.multiply, f"{a} * {b}", a, b)

            elif choice == "4":
                a = get_number("Enter numerator: ")
                b = get_number("Enter denominator: ")
                calculate(operations.divide, f"{a} / {b}", a, b)

            # Powers and roots

            elif choice == "5":
                a = get_number("Enter number: ")
                calculate(operations.square, f"{a}²", a)

            elif choice == "6":
                a = get_number("Enter number: ")
                calculate(operations.cube, f"{a}³", a)

            elif choice == "7":
                a = get_number("Enter number: ")
                calculate(operations.square_root, f"√({a})", a)

            elif choice == "8":
                a = get_number("Enter number: ")
                calculate(operations.cube_root, f"∛({a})", a)

            elif choice == "9":
                a = get_number("Enter base: ")
                b = get_number("Enter exponent: ")
                calculate(operations.power, f"{a} ^ {b}", a, b)

            elif choice == "10":
                a = get_number("Enter number: ")
                calculate(operations.reciprocal, f"1 / {a}", a)

            # Scientific operations

            elif choice == "11":
                a = get_number("Enter exponent: ")
                calculate(operations.exponential, f"e ^ {a}", a)

            elif choice == "12":
                a = get_number("Enter number: ")
                calculate(operations.natural_log, f"ln({a})", a)

            elif choice == "13":
                a = get_number("Enter number: ")
                calculate(operations.log_base_10, f"log10({a})", a)

            elif choice == "14":
                a = get_number("Enter angle in degrees: ")
                calculate(operations.sine, f"sin({a}°)", a)

            elif choice == "15":
                a = get_number("Enter angle in degrees: ")
                calculate(operations.cosine, f"cos({a}°)", a)

            elif choice == "16":
                a = get_number("Enter angle in degrees: ")
                calculate(operations.tangent, f"tan({a}°)", a)

            elif choice == "17":
                a = get_number("Enter a non-negative integer: ")

                if not a.is_integer():
                    raise ValueError(
                        "Factorial requires a non-negative integer."
                    )

                calculate(operations.factorial, f"{int(a)}!", a)

            elif choice == "18":
                a = get_number("Enter the original number: ")
                b = get_number("Enter percentage: ")
                calculate(
                    operations.percentage,
                    f"{b}% of {a}",
                    a,
                    b
                )

            # History management

            elif choice == "19":
                history.show_history()

            elif choice == "20":
                confirmation = input(
                    "Clear all calculation history? (y/n): "
                ).strip().lower()

                if confirmation == "y":
                    history.clear_history()
                else:
                    print("History was not cleared.")

            elif choice == "21":
                history.show_history()

                entries = history.load_history()

                if entries:
                    try:
                        index = int(
                            input("Enter the history entry number to delete: ")
                        )

                        deleted = history.delete_history_entry(index)

                        print(
                            f"Deleted: {deleted['expression']} "
                            f"= {deleted['result']}"
                        )

                    except ValueError:
                        print("Please enter a valid integer.")

            elif choice == "0":
                print("\nThank you for using the calculator!")
                break

            else:
                print("\nInvalid choice. Please select a valid option.")

        except (ValueError, ZeroDivisionError, OverflowError) as error:
            print(f"\nCalculation error: {error}")

        except OSError as error:
            print(f"\nFile operation error: {error}")


if __name__ == "__main__":
    main()