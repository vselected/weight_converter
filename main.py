def weight_converter():
    print("\n")
    print("Welcome to Weight Converter!")
    print("Please pick number for specific Unit:")
    print("Kilograms: 1")
    print("Pounds: 2")

    while True:

        unit_convert_from = input("Please provide unit you want to convert from: ")

        # Check if user operator choice is valid
        if unit_convert_from not in ["1", "2"]:
            print("Invalid choice. Please select a valid option.")
            continue

        unit_convert_to = input("Please provide unit you want to convert to: ")

        # Check if user operator choice is valid
        if unit_convert_to not in ["1", "2"]:
            print("Invalid choice. Please select a valid option.")
            continue

        # Function that convert
        if unit_convert_from == "1":
            if unit_convert_to == "1":
                weight = float(input("Please provide weight: "))
                print(f"{weight} Kilograms")
        elif unit_convert_from == 2:
            if unit_convert_to == 2:
                weight = float(input("Please provide weight: "))
                print(f"{weight} Pounds")

        # Create function that ask if you wanna still use converter
        next_convert = input("Do you want to do next convert? (y / n): ").lower()
        if next_convert != "y":
            print("Thank you for using Weight Converter!")
            break

# Run Program
weight_converter()