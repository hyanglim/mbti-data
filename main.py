import streamlit as st
import pandas as pd
import altair as alt

st.title("MBTI 유형별 상위 10개국 시각화")

# CSV 파일 업로드
uploaded_file = st.file_uploader("MBTI 국가별 데이터 CSV 파일 업로드", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("CSV 파일이 성공적으로 업로드되었습니다!")

    mbti_types = [
        'INFJ', 'ISFJ', 'INTP', 'ISFP', 'ENTP', 'INFP',
        'ENTJ', 'ISTP', 'INTJ', 'ESFP', 'ESTJ', 'ENFP',
        'ESTP', 'ISTJ', 'ENFJ', 'ESFJ'
    ]

    selected_type = st.selectbox("MBTI 유형 선택", mbti_types)

    # 상위 10개국 추출
    top_10 = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False).head(10)
    top_10[selected_type] = top_10[selected_type] * 100  # 퍼센트 단위로 변환

    st.subheader(f"{selected_type} 유형 비율 상위 10개국")

    # Altair 차트
    chart = alt.Chart(top_10).mark_bar().encode(
        x=alt.X('Country:N', sort='-y', title="국가"),
        y=alt.Y(f'{selected_type}:Q', title=f'{selected_type} 비율 (%)'),
        color=alt.Color(f'{selected_type}:Q', scale=alt.Scale(scheme='blues')),
        tooltip=['Country', selected_type]
    ).properties(
        width=600,
        height=400,
        title=f"{selected_type} 유형 비율 상위 10개국 (Altair 시각화)"
    )

    st.altair_chart(chart, use_container_width=True)

else:
    st.warning("CSV 파일을 먼저 업로드해주세요.")
