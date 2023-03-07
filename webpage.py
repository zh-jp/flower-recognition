import streamlit as st
import tensorflow as tf
import os
from PIL import Image
import numpy as np
import cv2
import train.train_model as train_model
import time


cache_path = 'D:/flowers-recognition-cache/'
# 顺序为：['dandelion', 'morning_glory', 'peony', 'plumeria_ubra', 'roses', 'sunflowers', 'tulips']
class_names = ['蒲公英', '牵牛花', '牡丹', '鸡蛋花', '玫瑰花', '向日葵', '郁金香']
if os.path.exists(cache_path) is False:
    os.mkdir(cache_path)
model = tf.keras.models.load_model('train/models/cnn_flower.h5')
model_transfer = tf.keras.models.load_model('train/models/mobilenet_flower.h5')
def main_windows():
    st.title('基于Tensorflow的花卉识别')

    option = st.selectbox(
        '-------',
        ('花卉图片识别', '训练（训练需较多时间等待）')
    )
    st.markdown('选择了' + '*' + option + "*")
    if option == '花卉图片识别':
        # 模型选择
        model_option = st.selectbox(
            '模型选择栏',
            ('自训练模型', 'mobilenet模型（迁移学习模型）')
        )
        st.markdown('选择了' + '*' + model_option + "*")
        model_name = model_option
        upload_file = st.file_uploader(label="$$图片上传$$", type=['png', 'jpg', 'jpeg'])
        if upload_file is not None:
            file = cache_path + '/' + upload_file.name
            with open(file, 'wb') as f:  # 将图片存入本地缓存
                f.write(upload_file.read())
            st.markdown(
                "<style>div.stButton > button:first-child {background-color: #4CAF50; color: white; width: 700px; "
                "}</style>",
                unsafe_allow_html=True,
            )
            click = st.button('Predict')
            st.image(upload_file)
            st.markdown('文件名为：' + '`' + upload_file.name + '`')
            if click:
                # 显示进度条
                progress_text = "图片识别中..."
                percent_complete = 0
                my_bar = st.progress(percent_complete, text=progress_text)
                time.sleep(1)
                percent_complete = 100
                progress_text = "识别完成，结果是..."
                my_bar.progress(percent_complete, text=progress_text)
                outputs = predict(file, model_name)
                st.success('该图片可能是：'+outputs)
                st.balloons()
    else:
        st.markdown(
            "<style>div.stButton > button:first-child {background-color: #FF66CC; color: white; width: 700px; }</style>",
            unsafe_allow_html=True,
        )
        click = st.button('Train')
        if click:

            # 显示进度条
            # progress_text = "模型训练中..."
            # percent_complete = 0
            # my_bar = st.progress(percent_complete, text=progress_text)
            # time.sleep(60 * 20)
            # percent_complete = 100
            # progress_text = '模型训练完成'
            # my_bar.progress(percent_complete, text=progress_text)
            os.system('python ./train/train_model.py')
            train_model.train(epochs=10, is_transfer=False)


def predict(file: str, model_name) -> str:
    img_init = cv2.imread(file)
    img_init = cv2.resize(img_init, (224, 224))
    cv2.imwrite(file, img_init)

    img = Image.open(file)
    img = np.asarray(img)
    if model_name == '自训练模型':
        outputs = model.predict(img.reshape(1, 224, 224, 3))
    else:
        outputs = model_transfer.predict(img.reshape(1, 224, 224, 3))
    result_index = np.argmax(outputs)
    result = class_names[result_index]
    return result


def side_bar():
    st.sidebar.image('imgs/side_bar.jpg')
    st.sidebar.title('Authors')
    st.sidebar.markdown('[郑金鹏](https://github.com/zh-jp)')
    st.sidebar.markdown('[范沛广](https://github.com/fpgboy)')
    st.sidebar.markdown('[丁文涛](https://github.com/miku122)')
    st.sidebar.markdown('[谭楚飞]()')
    st.sidebar.markdown('[钱炫任]()')
    st.sidebar.title('相关文档')
    st.sidebar.markdown(
        '[花卉识别任务书](https://github.com/zh-jp/flower-recognition/blob/main/%E8%8A%B1%E5%8D%89%E8%AF%86%E5%88%AB.docx)')
    st.sidebar.markdown(
        '[PPT](https://github.com/zh-jp/flower-recognition/blob/main/%E7%AD%94%E8%BE%A9PPT.pptx)')


def train_page():
    pass


if __name__ == "__main__":
    main_windows()
    side_bar()
