def weight_converter():

    while True:

        # Create function that ask if you wanna still use converter
        next_convert = input("Do you want to do next convert? (y / n): ").lower()
        if next_convert != "y":
            print("Thank you for using Weight Converter!")
            break

# Run Program
weight_converter()