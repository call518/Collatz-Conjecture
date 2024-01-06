import streamlit as st
import plotly.graph_objects as go
import time

MIN_VALUE = 3  # 글로벌 변수 설정

st.set_page_config(page_title="Collatz Conjecture Visualization (Maximum Value)", layout="wide", page_icon="🌀")

st.markdown("# Collatz Conjecture Visualization (Maximum Value)")
st.sidebar.header("Input Range of Numbers")
st.write(
    """This demo finds the starting numbers within a given range that produce the highest value in their Collatz sequences and visualizes them."""
)

def collatz(n):
    """Return the Collatz sequence for a given number and its max value."""
    sequence = []
    max_value = n
    while n != 1:
        sequence.append(n)
        if n > max_value:
            max_value = n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    sequence.append(1)
    return sequence, max_value

# 범위 입력
start_number = st.sidebar.number_input("Start number", min_value=MIN_VALUE, value=MIN_VALUE, step=1)
end_number = st.sidebar.number_input("End number", min_value=start_number, value=start_number + 10, step=1)

start_button = st.sidebar.button("Find Max Value and Visualize")

if start_button:
    max_values = {}
    highest_max_value = 0

    # 백그라운드에서 각 시작 값에 대한 최대 Y값 찾기
    for num in range(start_number, end_number + 1):
        _, current_max = collatz(num)
        max_values[num] = current_max
        if current_max > highest_max_value:
            highest_max_value = current_max

    # 최대 Y값을 가진 시작 값들 찾기
    max_start_numbers = [num for num, max_val in max_values.items() if max_val == highest_max_value]

    # 찾은 시작 값들에 대한 시퀀스를 차트에 그리기
    fig = go.Figure()
    for num in max_start_numbers:
        values = collatz(num)[0]
        fig.add_trace(go.Scatter(x=list(range(len(values))), y=values, mode='lines+markers', name=f'Start: {num}'))
    fig.update_layout(height=600, showlegend=True)

    chart_placeholder = st.plotly_chart(fig, use_container_width=True)