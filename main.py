def weight_converter():
    print("\n")
    print("Welcome to Weight Converter!")

    while True:

        print("Please pick number for specific Unit:")
        print("Kilograms: 1")
        print("Pounds: 2")

        unit_convert_from = int(input("Please provide unit you want to convert from: "))
        unit_convert_to = int(input("Please provide unit you want to convert to: "))
        weight = float(input("Please provide weight: "))

        # Create function that ask if you wanna still use converter
        next_convert = input("Do you want to do next convert? (y / n): ").lower()
        if next_convert != "y":
            print("Thank you for using Weight Converter!")
            break

# Run Program
weight_converter()