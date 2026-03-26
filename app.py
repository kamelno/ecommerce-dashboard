import pandas as pd
import streamlit as st
import plotly.express as px
import time
from analytics import EcommerceAnalytics

# إعدادات الصفحة (Pro Look)
st.set_page_config(page_title="Pro E-commerce Dashboard", layout="wide", page_icon="📊")
st.title("Real-Time E-commerce Analytics")

# تهيئة المحرك
analytics = EcommerceAnalytics()

# استخدام الـ Session State لتخزين البيانات عشان تفضل تتحدث
if 'main_df' not in st.session_state:
    st.session_state.main_df = analytics.generate_mock_data(20)

# --- Sidebar ---
st.sidebar.header("Control Panel")
refresh_rate = st.sidebar.slider("Refresh Rate (seconds)", 1, 10, 3)
if st.sidebar.button("Clear Data"):
    st.session_state.main_df = analytics.generate_mock_data(1)

# --- Dashboard Logic ---
placeholder = st.empty()

while True:
    # 1. تحديث البيانات (محاكاة لوصول أوردر جديد)
    new_data = analytics.generate_mock_data(1)
    st.session_state.main_df = pd.concat([st.session_state.main_df, new_data]).tail(100) # بنحتفظ بآخر 100 أوردر بس
    
    df = st.session_state.main_df
    rev, orders, avg = analytics.calculate_kpis(df)

    with placeholder.container():
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Revenue", f"${rev:,.2f}", delta=f"{new_data['price'].iloc[0]:.2f} New")
        col2.metric("Total Orders", orders)
        col3.metric("Avg Order Value", f"${avg:,.2f}")

        st.markdown("---")

        fig_col1, fig_col2 = st.columns(2)
        
        with fig_col1:
            st.subheader("Sales by Category")
            fig = px.pie(df, values='price', names='category', hole=0.4, 
                         color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig, use_container_width=True)

        with fig_col2:
            st.subheader("Live Sales Trend")
            fig2 = px.line(df, x='order_id', y='price', markers=True)
            st.plotly_chart(fig2, use_container_width=True)

        st.subheader("Recent Transactions")
        st.dataframe(df.sort_values(by='order_id', ascending=False), use_container_width=True)

    time.sleep(refresh_rate)