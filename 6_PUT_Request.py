    # PUT Request 
       # Update all data

import requests

link = "https://jsonplaceholder.typicode.com/posts/1";
data= {
    "id" : 101,
    "title" : "Updated Title",
    "userId" : 101,
};

respone = requests.put(link, json=data);

print(respone.json());