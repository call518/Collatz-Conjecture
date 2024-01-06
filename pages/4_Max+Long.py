import streamlit as st
import plotly.graph_objects as go

MIN_VALUE = 3  # 글로벌 변수 설정

st.set_page_config(page_title="Collatz Conjecture Visualization (Max/Long)", layout="wide", page_icon="🌀")

st.markdown("# Collatz Conjecture Visualization (Max/Long)")
st.sidebar.header("Input Range of Numbers")
st.write(
    """This demo visualizes the maximum value and the number of steps for each starting number in the Collatz Conjecture within a given range."""
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

start_button = st.sidebar.button("Visualize Data")

if start_button:
    max_values = []
    step_counts = []

    # 각 시작 값에 대한 최대값과 단계 수 계산
    for num in range(start_number, end_number + 1):
        sequence, max_val = collatz(num)
        max_values.append(max_val)
        step_counts.append(len(sequence))

    # 첫 번째 차트: 최대값
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=list(range(start_number, end_number + 1)), y=max_values, mode='lines+markers', marker=dict(size=2), line=dict(width=0.5)))
    fig1.update_layout(title="Maximum Value in Collatz Sequence", xaxis_title="Start Number", yaxis_title="Maximum Value", height=600)

    # 두 번째 차트: 단계 수
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=list(range(start_number, end_number + 1)), y=step_counts, mode='lines+markers', marker=dict(size=2), line=dict(width=0.5)))
    fig2.update_layout(title="Number of Steps in Collatz Sequence", xaxis_title="Start Number", yaxis_title="Number of Steps", height=600)

    # 차트 표시
    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
