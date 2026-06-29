import os
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "test_results.txt")

test_results = [
    {"test": "Login", "status": "PASSED"},
    {"test": "Logout", "status": "PASSED"},
    {"test": "Register", "status": "FAILED"},
    {"test": "Profile Update", "status": "PASSED"},
]

passed = 0
failed = 0

with open(file_path, "w") as file:
    file.write("Test Results\n")
    file.write("---\n")
    for i, result in enumerate(test_results, 1):
        file.write(f"Test {i}: {result['test']} - {result['status']}\n")
        if result['status'] == "PASSED":
            passed += 1
        else:
            failed += 1
    file.write("---\n")
    file.write(f"Total: {len(test_results)} | Passed: {passed} | Failed: {failed}\n")

print("Test report written!")
