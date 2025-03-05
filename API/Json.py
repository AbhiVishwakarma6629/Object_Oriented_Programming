import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print("First Post : ")
#     print("Title : ", data[0]['title'])
#     print("Body : ", data[0]['body'])
# else:
#     print("Invalid")




import requests

url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data[1] == 2:
        print("Name : ", data[0]['name'])
else:
    print("No data found")