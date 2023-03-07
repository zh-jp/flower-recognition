import streamlit as st
import tensorflow as tf
import os
from PIL import Image
import numpy as np
import cv2

model = tf.keras.models.load_model('train/models/cnn_flower.h5')
cache_path = 'D:/flowers-recognition-cache/'
# 顺序为：['dandelion', 'morning_glory', 'peony', 'plumeria_ubra', 'roses', 'sunflowers', 'tulips']
class_names = ['蒲公英', '牵牛花', '牡丹', '鸡蛋花', '玫瑰花', '向日葵', '郁金香']
if os.path.exists(cache_path) is False:
    os.mkdir(cache_path)


def main_windows():
    st.title('基于Tensorflow的花卉识别')

    option = st.selectbox(
        '-------',
        ('测试', '训练（训练需较多时间等待）')
    )
    st.markdown('选择了' + '*' + option[:2] + "*")
    if option == '测试':
        upload_file = st.file_uploader(label="$$图片上传$$", type=['png', 'jpg', 'jpeg'])
        if upload_file is not None:
            file = cache_path + '/' + upload_file.name
            with open(file, 'wb') as f:  # 将图片存入本地缓存
                f.write(upload_file.read())
            st.markdown(
                "<style>div.stButton > button:first-child {background-color: #4CAF50; color: white; width: 700px; }</style>",
                unsafe_allow_html=True,
            )
            click = st.button('Predict')
            st.image(upload_file)
            st.markdown('文件名为：' + '`' + upload_file.name + '`')
            outputs = ''
            if click:
                outputs = predict(file)
            st.write(outputs)
    else:
        pass


def predict(file: str) -> str:
    img_init = cv2.imread(file)
    img_init = cv2.resize(img_init, (224, 224))
    cv2.imwrite(file, img_init)

    img = Image.open(file)
    img = np.asarray(img)
    outputs = model.predict(img.reshape(1, 224, 224, 3))
    result_index = np.argmax(outputs)
    # print(result_index)
    result = class_names[result_index]
    return result


def side_bar():
    st.sidebar.title('Authors')
    st.sidebar.markdown('[郑金鹏](https://github.com/zh-jp)')
    st.sidebar.markdown('[范沛广](https://github.com/fpgboy)')
    st.sidebar.markdown('[丁文涛](https://github.com/miku122)')
    st.sidebar.title('相关文档')
    st.sidebar.markdown(
        '[花卉识别任务书](https://github.com/zh-jp/flower-recognition/blob/main/%E8%8A%B1%E5%8D%89%E8%AF%86%E5%88%AB%E4%BB%BB%E5%8A%A1%E4%B9%A6V1.0.docx)')
    st.sidebar.markdown(
        '[PPT](https://github.com/zh-jp/flower-recognition/blob/main/%E9%A1%B9%E7%9B%AE%E5%90%8D%E7%A7%B0%EF%BC%88%E6%A8%A1%E6%9D%BF%EF%BC%89.pptx)')


def train_page():
    pass


if __name__ == "__main__":
    main_windows()
    side_bar()
