import requests
import streamlit as st
import pandas as pd
import datetime as dt

st.set_page_config(page_title='주식 차트')
def get_stock(code, startdate, enddate):
    url = f'https://m.stock.naver.com/front-api/external/chart/domestic/info?symbol={code}&requestType=1&startTime={startdate}&endTime={enddate}&timeframe=day'
    response = requests.get(url)
    res = eval(response.text.replace('\n', '').replace('\t',''))

    df = pd.DataFrame(res[1:], columns=res[0])

    return df

st.title('주식 차트')

startdate = st.sidebar.date_input('조회 시작 일자', dt.datetime(2024,1,1))
enddate = st.sidebar.date_input('조회 종료 일자', dt.datetime(2024,1,1))
code = st.sidebar.text_input('종목코드 입력')

if startdate and enddate and code:
    df = get_stock(code, startdate.strftime('%Y%m%d'), enddate.strftime('%Y%m%d'))
    st.line_chart(df['종가'])
    st.bar_chart(df['거래량'])