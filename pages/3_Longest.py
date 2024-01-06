import streamlit as st
import plotly.graph_objects as go

MIN_VALUE = 3  # 글로벌 변수 설정

st.set_page_config(page_title="Collatz Conjecture Visualization (Longest Sequence)", layout="wide", page_icon="🌀")

st.markdown("# Collatz Conjecture Visualization (Longest Sequence)")
st.sidebar.header("Input Range of Numbers")
st.write(
    """This demo finds the starting number within a given range that produces the longest sequence in its Collatz sequence and visualizes it."""
)

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

start_button = st.sidebar.button("Find Longest Sequence and Visualize")

if start_button:
    longest_length = 0
    longest_start_number = start_number

    # 백그라운드에서 가장 긴 시퀀스를 생성하는 시작 값 찾기
    for num in range(start_number, end_number + 1):
        current_sequence = collatz(num)
        if len(current_sequence) > longest_length:
            longest_length = len(current_sequence)
            longest_start_number = num

    # 찾은 시작 값에 대한 시퀀스를 차트에 그리기
    values = collatz(longest_start_number)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(len(values))), y=values, mode='lines+markers', name=f'Start: {longest_start_number}'))
    fig.update_layout(height=600, showlegend=True)

    chart_placeholder = st.plotly_chart(fig, use_container_width=True)
