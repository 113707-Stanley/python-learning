import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "test_results1.txt")

try:
    with open(file_path, "r") as file:
        contents = file.read()
        print(f"File contents:\n{contents}")

except FileNotFoundError:
    print(f"Test results file not found — has the test suite run yet?")

except PermissionError:
    print(f"Cannot access file — check your permissions!")

else:
    print(f"File read successfully!")

finally:
    print(f"File operation complete.")