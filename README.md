# Cryptocurrency prices dashboard
This Streamlit app is [deployed on Streamlit Sharing](https://share.streamlit.io/). You can also clic on this [link]() to visualize the dashboard.

This dashboard represents the change of the price for one hundred of the most popular cryptocurrencies over the last year.

## Set Up

Create a python virtual environment and check the following requirements :

```
- Python version: 3.9.13
- Requests version: 2.28.2
- Pandas version:  1.5.3
- Streamlit version:  1.18.1
```

## Data

<code>assets_prices_history.csv</code>: data on the cryptocurrencies prices over the last 365 days. Can be found [here](https://docs.coincap.io/).

<code>get_API_data_to_CSV.py</code>: script for updating the data.


## Launching the App

Run the following line in the terminal, it will launch the Dashboard locally in the default browser.

```
streamlit run streamlit_app.py
```