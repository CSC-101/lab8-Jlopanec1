import sys

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide the name of the file to open.")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                try:
                    values = line.split()
                    if len(values) != 2:
                        print(f"Error: Line must contain exactly two values: {line}")
                        continue
                    num1 = float(values[0])
                    num2 = float(values[1])
                    print(f"Sum of {num1} and {num2} is {num1 + num2}")
                except ValueError:
                    print(f"Error: Invalid number in line: {line}")
                    continue
    except FileNotFoundError:
        print(f"Error: The file '{filename}' could not be found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
