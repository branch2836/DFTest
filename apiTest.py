import http.client

if __name__ == "__main__":
    conn = http.client.HTTPSConnection("api.cfl.ca")

    headers = {
        'key': "T8Mv9BRDdcB7bMQUsQvHqtCGPewH5y8p "
      
    }

    conn.request("GET", "/v1/teams/", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))