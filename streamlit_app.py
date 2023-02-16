import streamlit as st
import pandas as pd
import altair as alt
from datetime import date

st.title("Cryptocurrency prices dashboard")
st.write("""This dashboard represents the price change of one hundred most popular cryptocurrencies 
over the last year. The data obtained from https://docs.coincap.io/""")

st.sidebar.info(
    """
    This app is the test dashboard. You can find the GIT repository via this link https://github.com/AntonIOC777/dashboard_cryptocurrencies/
    """
)

DATA = "assets_prices_history.csv"
DATE_COLUMN = "date"


@st.cache_data
def load_data():
    df1 = pd.read_csv(DATA, parse_dates=[DATE_COLUMN])
    return df1


df = load_data()

min_date = min(df[DATE_COLUMN])
max_date = max(df[DATE_COLUMN])
assets_list = df.columns.tolist()
assets_list.remove(DATE_COLUMN)

with st.sidebar:
    option = st.selectbox("Select an asset", assets_list)
    st.write("Select the timeframe below:")
    date1, date2 = st.columns(2)
    with date1:
        date_from = st.date_input("Date from", min_date, min_value=min_date, max_value=date.today())
    with date2:
        date_to = st.date_input("Date to", max_date, min_value=min_date, max_value=date.today())

date_slice_df = df.loc[
    (df[DATE_COLUMN] >= pd.to_datetime(date_from)) & (df[DATE_COLUMN] <= pd.to_datetime(date_to)), [DATE_COLUMN,
                                                                                                    option]]
prev = alt.Chart(date_slice_df[[DATE_COLUMN, option]]).mark_bar().encode(x=DATE_COLUMN, y=option)
st.altair_chart(prev, use_container_width=True)
