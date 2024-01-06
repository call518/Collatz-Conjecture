import streamlit as st
import numpy as np
import time
import plotly.graph_objects as go

MIN_VALUE = 3  # 글로벌 변수 설정

st.set_page_config(page_title="Collatz Conjecture Visualization (Basic)", layout="wide", page_icon="🌀")

st.markdown("# Collatz Conjecture Visualization (Basic)")
st.sidebar.header("Input Number")
st.write(
    """This demo visualizes the Collatz Conjecture. Enter a number (3 or higher) and watch the sequence unfold in real-time!"""
)

# 로그 스케일 적용 여부 체크박스
log_scale = st.sidebar.checkbox("Apply Log Scale to Chart")

def collatz(n):
    """Return the next number in the Collatz sequence."""
    return n // 2 if n % 2 == 0 else 3 * n + 1

number = st.sidebar.number_input("Enter a number", min_value=1, value=1000, step=1)
start_button = st.sidebar.button("Start Visualization")

# 차트 위치를 미리 확보
chart_placeholder = st.empty()

if start_button:
    if number < MIN_VALUE:
        st.error(f"Number must be {MIN_VALUE} or higher!")  # 에러 메시지 표시
        chart_placeholder.empty()  # 차트 초기화
    else:
        progress_bar = st.sidebar.progress(0)
        status_text = st.sidebar.empty()
        values = [number]
        fig = go.Figure(go.Scatter(x=list(range(len(values))), y=values, mode='lines+markers'))
        if log_scale:
            fig.update_layout(height=600, yaxis_type="log")
        else:
            fig.update_layout(height=600)
        chart = chart_placeholder.plotly_chart(fig, use_container_width=True)

        i = 0
        while values[-1] != 1:
            new_value = collatz(values[-1])
            values.append(new_value)
            fig = go.Figure(go.Scatter(x=list(range(len(values))), y=values, mode='lines+markers'))
            if log_scale:
                fig.update_layout(height=600, yaxis_type="log")
            else:
                fig.update_layout(height=600)
            chart.plotly_chart(fig, use_container_width=True)

            progress = int((i / (i + np.log2(values[-1]))) * 100)
            progress_bar.progress(progress)
            status_text.text(f"Current Value: {values[-1]}")
            time.sleep(0.05)
            i += 1

        progress_bar.empty()
