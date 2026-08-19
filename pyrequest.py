import requests
from datetime import datetime 


print("==================")
print("     PyRequest    ")
print("==================")

print("OPTIONS:")
print("1. GET Request")
print("2. POST Request")
print("3. Quit")

while True:
    try:
        option = int(input("Select an Option: "))

        if option == 1:
            action = "GET"

            print("Leave empty for /")
            path = input("Path/Route: ")

            url = "http://127.0.0.1:8000" + path

            request = requests.get(
                url=url
            )

            now = datetime.now()
            with open("logs.txt", "a") as file:
                file.write(f"Time(S:M:Y): {now.strftime("%S:%M:%H")}\n")
                file.write(f"Action: {action}\n")
                file.write(f"Response Headers: {request.headers}\n")
                file.write("-" * 50 + "\n")

            print(f"Status Code: {request.status_code}")
            print(f"Output: {request.text}")
            print(f"Logs saved in logs.txt")
            break
        elif option == 2:
            action = "POST"

            print("Leave empty for /")
            path = input("Path/Route: ")
            data = input("Data: ")

            url = "http://127.0.0.1:8000" + path

            request = requests.post(
                url=url,
                data=data
            )

            now = datetime.now()
            with open("logs.txt", "a") as file:
                file.write(f"Time(S:M:Y): {now.strftime("%S:%M:%H")}\n")
                file.write(f"Action: {action}\n")
                file.write(f"Response Headers: {request.headers}\n")
                file.write("-" * 50 + "\n")

            print(f"Status Code: {request.status_code}")
            print(f"Output: {request.text}")
            print(f"Logs saved in logs.txt")
            break
        elif option == 3:
            break
        else:
            print("Enter a valid Option!")
            continue
    except ValueError:
        print("Enter a valid number!")
        continue
