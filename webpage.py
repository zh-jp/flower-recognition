import streamlit as st


def main_windows():
    st.title('基于tensorflow的花卉识别')


def side_bar():
    st.sidebar.title('Authors')
    st.sidebar.markdown('[郑金鹏](https://github.com/zh-jp)')
    st.sidebar.markdown('[范沛广](https://baidu.com)')
    st.sidebar.markdown('[丁文涛](https://github.com/miku122)')
    st.sidebar.title('训练 OR 测试')
    option = st.sidebar.selectbox(
        '训练需较多时间等待',
        ('训练', '测试')
    )
    st.sidebar.markdown('选择了' + '*' + option + "*")
    st.sidebar.html('<p style="color:red">hello</p>')

if __name__ == "__main__":
    main_windows()
    side_bar()