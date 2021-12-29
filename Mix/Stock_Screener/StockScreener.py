from Keys import TD_AMERI_key as tak
import pandas as pd
import requests
import time
import re
import pickle as pkl
import os

# Reading the excel file that has company symbols/names
df = pd.read_excel("company_list.xlsx")
# Extracting the symbols column from the dataFrame and storing it as a list
symbols = df["Symbol"].values.tolist()

url = "https://api.tdameritrade.com/v1/instruments"

start = 0
end = 500
files = []
while start < len(symbols):
    tickers = symbols[start:end]

    payload = {"apikey": tak,
               "symbol": tickers,
               "projection": "fundamental"
               }
    results = requests.get(url, params=payload)
    data = results.json()
    f_name = time.asctime() + ".pkl"
    f_name = re.sub("[ :]", "_", f_name)
    files.append(f_name)
    with open(f_name, "wb") as file:
        pkl.dump(data, file)
    start = end
    end += 500
    time.sleep(1)

data = []

for file in files:
    with open(file, "rb") as f:
        info = pkl.load(f)
    tickers = list(info)
    points = ["symbol", "netProfitMarginMRQ", "peRatio", "pegRatio", "high52"]
    for ticker in tickers:
        tick = []
        for point in points:
            tick.append(info[ticker]["fundamental"][point])
        data.append(tick)
    os.remove(file)

points = ["symbol", "Margin", "PE", "PEG", "high52"]

df_results = pd.DataFrame(data, columns=points)

df_peg = df_results[(df_results["PEG"] < 1) & (df_results["PEG"] > 0) & (df_results["Margin"] > 20) &
                    (df_results["PE"] > 10)]


def view(size):
    start = 0
    stop = size
    while stop < len(df_peg):
        print(df_peg[start:stop])
        start = stop
        stop += size
    print(df_peg[start:stop])


# df_peg.sort_values(["PEG"])
# print(df_peg.shape[0])
# print(view(10))


