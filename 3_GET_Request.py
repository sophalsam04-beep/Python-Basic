    # GET Requests
import requests

url = "https://jsonplaceholder.typicode.com/users";

respone = requests.get(url);
  # checking status code
print(respone.status_code);
   # from the json API
print(respone.json());