import requests
import pandas as pd


def fetch_asset_data(asset_name):
    response = requests.get(f'https://api.coincap.io/v2/assets/{asset_name}/history?interval=d1').json()["data"]
    df = pd.DataFrame(response)
    df.drop(["date"], inplace=True, axis=1)
    df["time"] = pd.to_datetime(df["time"], unit="ms")
    df.rename(columns={"time": "date", "priceUsd": f"{asset_name}"}, inplace=True)
    new_cols = ["date", f"{asset_name}"]
    df = df.reindex(columns=new_cols)
    return df


def fetch_history(url):
    response = requests.get(url).json()["data"]
    info_df = pd.DataFrame(response)
    asset_ids = info_df["id"].tolist()
    for asset in asset_ids:
        if asset == "bitcoin":
            df = fetch_asset_data(asset)["date"]
        df = pd.concat([df, fetch_asset_data(asset)[f'{asset}']], axis=1)
    df.to_csv("assets_prices_history.csv", index=False)


fetch_history("https://api.coincap.io/v2/assets")