import sys

def main():
    # Check if a file name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Error: Please provide the name of a file to read.")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split()
                if len(parts) != 2:
                    print(f"Error: Line does not contain exactly two values: {line}")
                    continue
                try:

                    value1 = float(parts[0])
                    value2 = float(parts[1])

                    print(f"The sum of {value1} and {value2} is {value1 + value2}")

                except ValueError:

                    print(f"Error: Could not convert values to floats: {line}")
                    continue
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
if __name__ == "__main__":
    main()