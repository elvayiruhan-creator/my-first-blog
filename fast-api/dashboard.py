import streamlit as st
import seaborn as sns
from matplotlib import pyplot as plt

@st.cache_data 
def load_data():
    return sns.load_dataset('penguins')

df = load_data()

st.write("# Penguins Dashboard")

# 创建四个标签页
tab1, tab2, tab3, tab4 = st.tabs(["数据表格", "散点图", "直方图", "说明"])

# --- 第一个标签页：展示表格 ---
with tab1:
    st.write("### 企鹅原始数据前5行")
    st.write(df.head(5))

# --- 第二个标签页：展示散点图 ---
with tab2:
    st.write("### 喙部长度 vs 深度")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species", ax=ax)
    st.pyplot(fig)

# --- 第三个标签页：展示直方图 ---
with tab3:
    st.write("### 企鹅体重分布")
    fig2, ax2 = plt.subplots()
    sns.histplot(data=df, x="body_mass_g", kde=True, ax=ax2)
    st.pyplot(fig2)

# --- 第四个标签页 ---
with tab4:
    st.write("这是一个用 Streamlit 做的专业数据分析仪表盘。")