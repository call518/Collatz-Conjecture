import streamlit as st
import numpy as np
import time
import plotly.graph_objects as go

MIN_VALUE = 3  # 글로벌 변수 설정

st.set_page_config(page_title="Collatz Conjecture Visualization", layout="wide", page_icon="🌀")

st.markdown("# Collatz Conjecture Visualization")
st.sidebar.header("Collatz Conjecture")
st.write(
    """This demo visualizes the Collatz Conjecture. Choose to enter a single number or a range of numbers and watch the sequence unfold in real-time!"""
)

# 로그 스케일 적용 여부 체크박스
log_scale = st.sidebar.checkbox("Apply Log Scale to Chart")

# 단일 숫자 또는 범위 선택
range_input = st.sidebar.checkbox("Enter a range of numbers")

def collatz(n):
    """Return the next number in the Collatz sequence."""
    sequence = []
    while n != 1:
        sequence.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    sequence.append(1)
    return sequence

if range_input:
    start_number = st.sidebar.number_input("Start number", min_value=MIN_VALUE, value=MIN_VALUE, step=1)
    end_number = st.sidebar.number_input("End number", min_value=start_number, value=start_number + 10, step=1)
else:
    number = st.sidebar.number_input("Enter a number", min_value=MIN_VALUE, value=1000, step=1)

start_button = st.sidebar.button("Start Visualization")

# 차트 위치를 미리 확보
chart_placeholder = st.empty()

if start_button:
    fig = go.Figure()
    if range_input:
        for num in range(start_number, end_number + 1):
            values = collatz(num)
            fig.add_trace(go.Scatter(x=list(range(len(values))), y=values, mode='lines+markers', name=f'Start: {num}'))
        if log_scale:
            fig.update_layout(height=600, yaxis_type="log")
        else:
            fig.update_layout(height=600)
        chart_placeholder.plotly_chart(fig, use_container_width=True)
    else:
        values = collatz(number)
        fig.add_trace(go.Scatter(x=list(range(len(values))), y=values, mode='lines+markers'))
        if log_scale:
            fig.update_layout(height=600, yaxis_type="log")
        else:
            fig.update_layout(height=600)
        chart_placeholder.plotly_chart(fig, use_container_width=True)