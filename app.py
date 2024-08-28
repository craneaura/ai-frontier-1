import streamlit as st
import pandas as pd
from datetime import datetime

# 일정 데이터 저장용 DataFrame 초기화
if 'schedule_df' not in st.session_state:
    st.session_state.schedule_df = pd.DataFrame(columns=['날짜', '일정'])

# 날짜 선택
selected_date = st.date_input("날짜 선택", datetime.today())

# 일정 입력
task = st.text_input("일정 입력", placeholder="일정을 입력하세요")

# 일정 저장 버튼
if st.button("저장"):
    if task:
        # 데이터프레임에 일정 추가
        new_row = pd.DataFrame({'날짜': [selected_date], '일정': [task]})
        st.session_state.schedule_df = pd.concat([st.session_state.schedule_df, new_row], ignore_index=True)
        st.success(f"일정 '{task}'가 저장되었습니다.")
    else:
        st.error("일정을 입력하세요.")

# 저장된 일정 표시
st.subheader("저장된 일정")
if not st.session_state.schedule_df.empty:
    st.dataframe(st.session_state.schedule_df)
else:
    st.write("저장된 일정이 없습니다.")
