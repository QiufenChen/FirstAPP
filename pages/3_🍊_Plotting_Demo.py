#!/usr/bin/env python
# Author  : KerryChen
# File    : 3_🍊_Plotting_Demo.py
# Time    : 2024/8/8 14:18

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import gaussian_kde


# 模拟一些数据
data = pd.DataFrame({
    'X': np.arange(100),
    'Y': np.random.randn(100) * 5,
    'Category': np.random.choice(['A', 'B', 'C'], 100)
})

# 侧面板区域
st.sidebar.title("Plot Demo")
chart_list = ['Scatter Chart', 'Bar Chart', 'Line Chart', 'Density Chart', 'Histogram Chart', 'Scatter-Density']
selected_charts = st.sidebar.multiselect(label="Chart Types", options=chart_list)


# 主内容区域
st.header('Chart Selection and Display', divider="rainbow")

# 根据用户选择绘制图表
if 'Scatter Chart' in selected_charts:
    st.subheader('Scatter Chart')
    st.scatter_chart(data, x="X", y="Y", color="Category", use_container_width=True)
    # fig, ax = plt.subplots()
    # ax.scatter(data['X'], data['Y'])
    # st.pyplot(fig)

if 'Bar Chart' in selected_charts:
    st.subheader('Bar Chart')
    st.bar_chart(data, x="X", y="Y", color="Category")
    # fig, ax = plt.subplots()
    # ax.bar(data['X'], data['Y'])
    # st.pyplot(fig)

if 'Line Chart' in selected_charts:
    st.subheader('Line Chart')
    st.line_chart(data, x="X", y="Y", color="Category")
    # fig, ax = plt.subplots()
    # ax.plot(data['X'], data['Y'])
    # st.pyplot(fig)

if 'Histogram Chart' in selected_charts:
    st.subheader('Histogram Chart')
    fig, ax = plt.subplots(figsize=(10,8), dpi=600)
    ax.hist(data['Y'], bins=20)
    st.pyplot(fig)


if 'Density Chart' in selected_charts:
    st.subheader('Density Chart')
    fig, ax = plt.subplots(figsize=(10, 8), dpi=600)
    sns.kdeplot(data['Y'], fill=True, color='green')
    plt.xlabel('Y', fontsize=15, fontweight='bold')
    plt.ylabel('Density', fontsize=15, fontweight='bold')
    plt.legend()
    st.pyplot(plt)


if 'Scatter-Density' in selected_charts:
    st.subheader('Scatter-Density Chart')
    N = 1000
    X = np.random.normal(size=N)
    Y = X * 3 + np.random.normal(size=N)

    # Calculate the point density
    xy = np.vstack([X, Y])  # 将两个维度的数据叠加
    z = gaussian_kde(xy)(xy)  # 建立概率密度分布，并计算每个样本点的概率密度

    # Sort the points by density, so that the densest points are plotted last
    idx = z.argsort()
    x, y, z = X[idx], Y[idx], z[idx]

    fig, ax = plt.subplots(figsize=(10, 8), dpi=600)
    plt.scatter(x, y, c=z, s=20, cmap='Spectral')  # c表示标记的颜色
    plt.colorbar()
    st.pyplot(plt)
