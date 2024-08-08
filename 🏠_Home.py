import glob
import re
import streamlit as st
from PIL import Image

st.set_page_config(page_title="MyAPP",
                   page_icon=":four_leaf_clover:",
                   layout="wide",
                   initial_sidebar_state="auto")

st.title('Welcome to my :red[first Streamlit Webpage] :sunglasses:')
st.divider()

st.write("""This demo demonstrates how to use Markdown""")


# https://docs.streamlit.io/develop/api-reference/layout/st.sidebar
st.sidebar.success("Select a demo above")

files = glob.glob('files/*.md')
with open(files[0], 'r', encoding='utf-8') as info:
    markdown_text = info.read()


def render_markdown_with_images(markdown_text):
    # 匹配 Markdown 图片语法 ![alt text](image_url)
    pattern = re.compile(r'!\[.*?\]\((.*?)\)')

    # 记录上一个位置
    last_pos = 0

    # 查找所有匹配项
    for match in pattern.finditer(markdown_text):
        # 显示上一个位置到匹配位置之间的文本
        st.markdown(markdown_text[last_pos:match.start()], unsafe_allow_html=True)

        # 显示图片
        img_url = match.group(1)
        # print(img_url)
        img = Image.open
        st.image(img_url)

        # 更新上一个位置
        last_pos = match.end()

    # 显示剩余的文本
    st.markdown(markdown_text[last_pos:], unsafe_allow_html=True)


# 调用函数显示内容
render_markdown_with_images(markdown_text)


st.write(":blossom: Reference----> https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app")