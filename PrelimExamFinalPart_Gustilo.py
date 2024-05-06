class MultiplicationTable():
    def __init__(self, rows=5, cols=5):
        self.rows = rows
        self.cols = cols

    def input_table_size(self):
        self.rows = int(input("Enter the number of rows: "))
        self.cols = int(input("Enter the number of columns: "))

    def generate_table(self, odd_or_even="even"):
        """
        This prints a multiplication table with either even or odd numbers.

        Args:
            odd_or_even: A string, either "odd" or "even" to determine 
                         the type of product to display.
        """
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                product = i * j
                if (product % 2 == 0 and odd_or_even == "even") or \
                   (product % 2 == 1 and odd_or_even == "odd"):
                    print(f"{product}\t", end="")
            print()


# Example Usage
while True:  # Allow repeated use
    table_type = input("Display odd or even number products? (odd/even): ")
    if table_type.lower() not in ("odd", "even"):
        print("Invalid input. Please enter 'odd' or 'even'")
        continue  # Go back to asking for a valid choice

    table = MultiplicationTable()
    table.input_table_size()
    table.generate_table(table_type.lower())

    repeat = input("Do you want to generate another table? (yes/no): ")
    if repeat.lower() != "yes":
        break
