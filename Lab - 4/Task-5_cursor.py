def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"{filename} not found.")
        return 0

filename = "hw.txt"
num_lines = count_lines_in_file(filename)
print(f"file has {num_lines} lines")
