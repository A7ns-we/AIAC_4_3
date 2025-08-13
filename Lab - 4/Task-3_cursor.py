full_name = input("Enter your full name: ").strip()
parts = full_name.split()
if len(parts) >= 2:
    print(f"First name: {parts[0].lower()}")
    print(f"Last name: {parts[-1].lower()}")
else:
    print("Please enter at least a first and last name.")
