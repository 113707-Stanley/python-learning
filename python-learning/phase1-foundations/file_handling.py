import os
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "test_results.txt")

with open(file_path, "w") as file:
    file.write("Test Results\n")
    file.write("---\n")
    file.write("Test 1: Login - PASSED\n")
    file.write("Test 2: Logout - PASSED\n")
    file.write("Test 3: Register - FAILED\n")

print(f"File written to: {file_path}")

# Reading from a file
print(f"\nReading file contents:")
with open(file_path, "r") as file:
    contents = file.read()
    print(contents)

with open(file_path, "a") as file:
    file.write("Test 4: Profile Update - PASSED\n")

print(f"\nReading file contents:")
with open(file_path, "r") as file:
    contents = file.read()
    print(contents)
