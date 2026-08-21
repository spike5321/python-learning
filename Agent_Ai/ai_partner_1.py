import streamlit as st
st.set_page_config(
    page_title="AI Partner",
    page_icon="💞",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={},
)


#大标题
st.title("AI Partner")
st.logo("")
prompt = st.chat_input("请输入您的问题")
if prompt: 
    st.write(f"用户：{prompt}")
