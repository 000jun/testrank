import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.header('상승률 데이터', divider='rainbow')

# 데이터 불러오기
df = pd.read_excel('stock(%).xlsx')
df['순위'] = df['up/down(%)'].rank(ascending=False, method='min').astype(int)
df = df[['순위', 'Name', 'Symbol', 'Industry', 'up/down(%)', 'open_price', 'close_price', 'market', 'start_date', 'end_date', 'lower_name']]
df['up/down(%)'] = df['up/down(%)'].astype(int)



# 검색창
with st.expander('종목명 키워드 검색'):
    search_name = st.text_input('검색할 종목명을 입력하세요.(포함문자)', placeholder='ex) apple')
    search_result = df[df['lower_name'].str.contains(search_name)]
    st.dataframe(search_result)

with st.expander('전체 데이터'):
    st.dataframe(df)