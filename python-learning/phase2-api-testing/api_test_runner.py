import requests
import urllib3
import datetime
import os
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://jsonplaceholder.typicode.com"
REQUIRED_FIELDS = ["id", "name", "username", "email", "phone"]

def fetch_users():
    try:
        response = requests.get(f"{BASE_URL}/users", verify=False)
        return response.status_code, response.json()
    except requests.exceptions.ConnectionError:
        return None, None

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_required_fields(user):
    return all(field in user and user[field] for field in REQUIRED_FIELDS)

def validate_id_is_number(user):
    return isinstance(user['id'], int)

def run_tests(users, status_code):
    # Add this line at the top before your results = []
    ##users[0]['email'] = "not-a-valid-email"
    results = []
    
    # Test 1 - Status code check
    results.append({
        "id": 1,
        "name": "API Status Code Check",
        "status": "PASSED" if status_code == 200 else "FAILED",
        "detail": f"Expected 200, got {status_code}"
    })
    
    # Test 2 - User count check
    results.append({
        "id": 2,
        "name": "User Count Check",
        "status": "PASSED" if len(users) == 10 else "FAILED",
        "detail": f"Expected 10 users, got {len(users)}"
    })
    
    # Tests 3-5 - Per user validation
    for user in users:
        # Test 3 - Required fields
        results.append({
            "id": 3,
            "name": f"Required Fields Check — {user['name']}",
            "status": "PASSED" if validate_required_fields(user) else "FAILED",
            "detail": f"Checked fields: {REQUIRED_FIELDS}"
        })
        
        # Test 4 - Email validation
        results.append({
            "id": 4,
            "name": f"Email Format Check — {user['name']}",
            "status": "PASSED" if validate_email(user['email']) else "FAILED",
            "detail": f"Email: {user['email']}"
        })
        
        # Test 5 - ID is number
        results.append({
            "id": 5,
            "name": f"ID Type Check — {user['name']}",
            "status": "PASSED" if validate_id_is_number(user) else "FAILED",
            "detail": f"ID value: {user['id']}"
        })
    
    return results
def generate_report(results, file_path):
    try:
        passed = sum(1 for r in results if r['status'] == 'PASSED')
        failed = sum(1 for r in results if r['status'] == 'FAILED')
        total = len(results)
        pass_rate = (passed / total) * 100
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        divider = "=" * 60
        thin_divider = "-" * 60

        with open(file_path, "w", encoding="utf-8") as file:
            # Header
            file.write(f"API TEST REPORT\n")
            file.write(f"Generated: {timestamp}\n")
            file.write(f"API: {BASE_URL}\n")
            file.write(f"{divider}\n\n")

            # Test results
            file.write(f"TEST RESULTS\n")
            file.write(f"{thin_divider}\n")
            for result in results:
                icon = "✅" if result['status'] == "PASSED" else "❌"
                file.write(f"{icon} {result['name']}\n")
                file.write(f"   Detail: {result['detail']}\n")
                file.write(f"{thin_divider}\n")

            # Summary
            file.write(f"\nSUMMARY\n")
            file.write(f"{divider}\n")
            file.write(f"Total Tests : {total}\n")
            file.write(f"Passed      : {passed}\n")
            file.write(f"Failed      : {failed}\n")
            file.write(f"Pass Rate   : {pass_rate:.1f}%\n")
            file.write(f"{divider}\n")

            # Overall result
            overall = "✅ ALL TESTS PASSED" if failed == 0 else f"❌ {failed} TEST(S) FAILED"
            file.write(f"\nOVERALL RESULT: {overall}\n")

        print(f"Report generated successfully!")
        return True

    except PermissionError:
        print(f"Cannot write report — permission denied!")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
    
def read_report(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            print(f"\n{file.read()}")
    except FileNotFoundError:
        print("Report not found — generate it first!")

def main():
    print(f"Starting API Test Suite...")
    print(f"Target: {BASE_URL}\n")

    # Step 1 - Fetch data
    print(f"Fetching users from API...")
    status_code, users = fetch_users()

    # Step 2 - Check connection
    if users is None:
        print(f"Connection failed — cannot reach API!")
        return

    print(f"Fetched {len(users)} users successfully!")

    # Step 3 - Run tests
    print(f"Running tests...")
    results = run_tests(users, status_code)

    # Step 4 - Generate report
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "api_test_report.txt")
    success = generate_report(results, file_path)

    # Step 5 - Display report
    if success:
        read_report(file_path)

main()