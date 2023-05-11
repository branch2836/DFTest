import sys
from df_handler import DfHandler


if __name__ == "__main__":
    url = "https://my.api.mockaroo.com/schema1.json?min_age=10&max_age=80"
    # payload = { 'key': "ff8ad770"  }
    payload = {}

    pwd_str = sys.argv[1]
    spl_word = '='
    pwd = pwd_str.split(spl_word)[1]
    payload["key"] =pwd

    dfhandler = DfHandler()
    df = dfhandler.get_df_from_api(url, payload)
    df.show()

