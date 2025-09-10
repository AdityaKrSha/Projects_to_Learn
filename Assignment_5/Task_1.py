
students = {
    "Aditya": 85,
    "Rahul": 90,
    "Priya": 78,
    "Sneha": 92,
    "Amit": 88
}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks are: {students[name]}")
else:
    print(f"Sorry, no record found for {name}.")
