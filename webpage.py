import streamlit as st


def main_windows():
    st.title('基于tensorflow的花卉识别')
    option = st.selectbox(
        '-------',
        ('训练（训练需较多时间等待）', '测试')
    )
    st.markdown('选择了' + '*' + option[:2] + "*")
    if option == '测试':
        upload_file = st.file_uploader(label="$$图片上传$$", type=['png', 'jpg', 'jpeg'])
        if upload_file is not None:
            st.image(upload_file)
            st.markdown('文件名为：' + '`' + upload_file.name + '`')
    else:
        pass



def side_bar():
    st.sidebar.title('Authors')
    st.sidebar.markdown('[郑金鹏](https://github.com/zh-jp)')
    st.sidebar.markdown('[范沛广](https://github.com/fpgboy)')
    st.sidebar.markdown('[丁文涛](https://github.com/miku122)')
    st.sidebar.title('相关文档')
    st.sidebar.markdown('~这部分超链接后期要变更~')
    st.sidebar.markdown('[花卉识别任务书](https://github.com/zh-jp/flower-recognition/blob/main/%E8%8A%B1%E5%8D%89%E8%AF%86%E5%88%AB%E4%BB%BB%E5%8A%A1%E4%B9%A6V1.0.docx)')
    st.sidebar.markdown('[PPT](https://github.com/zh-jp/flower-recognition/blob/main/%E9%A1%B9%E7%9B%AE%E5%90%8D%E7%A7%B0%EF%BC%88%E6%A8%A1%E6%9D%BF%EF%BC%89.pptx)')


def train_page():
    pass



if __name__ == "__main__":
    main_windows()
    side_bar()