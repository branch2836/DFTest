import requests
from df_handler import get_df_from_api



if __name__ == "__main__":
    url = "https://my.api.mockaroo.com/schema1.json?min_age=10&max_age=80"

    payload = { 'key': "ff8ad770"  }

    r = get_df_from_api(url, payload)

    response = r.text.split('\n')
    columns = response.pop(0).split(',')
   
    data = []
    for line in response:
        if len(line) > 10:
            data.append(tuple(line.split(',')))
    
    print(data)

