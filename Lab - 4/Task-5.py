def count_lines_in_file(hw):
    try:
        with open(hw, 'r', encoding='utf-8') as file:
            return len(file.readlines())
    except FileNotFoundError:
        print(f"File '{hw}' not found.")
        return 0

# Example usage:
filename = "hw.txt"
lines = count_lines_in_file(filename)
print(f"The file contains {lines} lines")
