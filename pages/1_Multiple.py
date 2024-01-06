import streamlit as st
import plotly.graph_objects as go
import random

MIN_VALUE = 3  # 글로벌 변수 설정
MAX_LINES = 1000  # 최대 라인 수 설정

st.set_page_config(page_title="Collatz Conjecture Visualization (Multiple)", layout="wide", page_icon="🌀")

st.markdown("# Collatz Conjecture Visualization (Multiple)")
st.sidebar.header("Input Range of Numbers")
st.write(
    """This demo visualizes the Collatz Conjecture. Enter a range of numbers and watch the sequence unfold in real-time!"""
)

# 로그 스케일 및 랜덤 선택 체크박스
log_scale = st.sidebar.checkbox("Apply Log Scale to Chart")
random_selection = st.sidebar.checkbox("Random Selection")

def collatz(n):
    """Return the Collatz sequence for a given number."""
    sequence = []
    while n != 1:
        sequence.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    sequence.append(1)
    return sequence

# 범위 입력
start_number = st.sidebar.number_input("Start number", min_value=MIN_VALUE, value=MIN_VALUE, step=1)
end_number = st.sidebar.number_input("End number", min_value=start_number, value=start_number + 10, step=1)

start_button = st.sidebar.button("Start Visualization")

if start_button:
    numbers = list(range(start_number, end_number + 1))
    num_values = len(numbers)

    if random_selection:
        if num_values > MAX_LINES:
            numbers = random.sample(numbers, MAX_LINES)
        else:
            random.shuffle(numbers)
        numbers = sorted(numbers)  # 랜덤 선택 후 오름차순 정렬
    elif num_values > MAX_LINES:
        st.error(f"Error: The number of steps cannot exceed {MAX_LINES}.")
        st.stop()

    fig = go.Figure()
    for num in numbers:
        values = collatz(num)
        fig.add_trace(go.Scatter(x=list(range(len(values))), y=values, mode='lines+markers', name=f'Start: {num}'))
    if log_scale:
        fig.update_layout(height=600, yaxis_type="log")
    else:
        fig.update_layout(height=600)
    chart_placeholder = st.plotly_chart(fig, use_container_width=True)