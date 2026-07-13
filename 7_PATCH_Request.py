   # PATCH Request
      # Update field importants

import requests


url = "https://jsonplaceholder.typicode.com/posts/1";
data = {
    "title" : "Loving python...!",
};


respone = requests.patch(url, json=data);
print(respone.json());