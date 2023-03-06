import tensorflow as tf
import matplotlib.pyplot as plt

# 数据加载及划分，按照8:2的比例加载花卉数据
def data_load(data_dir, img_height, img_width, batch_size):
    #生成tf.data.Dataset类型的数据
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,                 #文件目录
        label_mode='categorical', #标签编码为分类向量
        validation_split=0.2,     #保留20%的数据用于验证集
        subset="training",        #80%的训练集
        seed=123,                 #设置用于shuffle和转换的可选随机种子
        image_size=(img_height, img_width),#图片大小
        batch_size=batch_size)    #设置数据批次的大小，默认为32

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        label_mode='categorical',
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size)

    class_names = train_ds.class_names

    return train_ds, val_ds, class_names


# 模型加载，指定图片处理的大小和是否进行迁移学习
def model_load(IMG_SHAPE=(224, 224, 3), is_transfer=False):
    if is_transfer:
        # 微调的过程中不需要对数据进行归一化的处理，此处我们采用已经封装好的MoblieNetV2模型
        base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE,  #设置图片大小
                                          include_top=False,                   #不加载顶层模型
                                          weights='imagenet')                  #使用ImageNet的参数初始化模型的参数
        base_model.trainable = False                                           #固定MoblieNetV2的权重
        #使用sequentail拼接网络结构
        model = tf.keras.models.Sequential([
            tf.keras.layers.experimental.preprocessing.Rescaling(1./127.5, offset=-1, input_shape=IMG_SHAPE),
            base_model,
            tf.keras.layers.GlobalAveragePooling2D(),      #平均值池化
            tf.keras.layers.Dense(7, activation='softmax') #自己设置顶层
        ])
    else:
        model = tf.keras.models.Sequential([
            #归一化，将像素值处理成0到1之间的值
            tf.keras.layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=IMG_SHAPE),
            #定义一个卷积层，使用32个3*3大小的卷积核，激活函数使用relu
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
            #最大值池化
            tf.keras.layers.MaxPooling2D(2, 2),

            #定义一个卷积层使用64个3*3大小的卷积核
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D(2, 2),
            #将多维特征值展开为向量
            tf.keras.layers.Flatten(),
            #使用一个128个结点的全连接层
            tf.keras.layers.Dense(128, activation='relu'),
            #输出顶层预测结果
            tf.keras.layers.Dense(7, activation='softmax')
        ])

    model.summary()
    # 模型训练
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model


# 展示训练过程的曲线
def show_loss_acc(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    plt.plot(acc, label='Training Accuracy')
    plt.plot(val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.ylabel('Accuracy')
    plt.ylim([min(plt.ylim()), 1])
    plt.title('Training and Validation Accuracy')

    plt.subplot(2, 1, 2)
    plt.plot(loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.ylabel('Cross Entropy')
    plt.ylim([0, 1.0])
    plt.title('Training and Validation Loss')
    plt.xlabel('epoch')
    plt.show()


def train(epochs, is_transfer=False):

    #加载数据
    train_ds, val_ds, class_names = data_load("./data/flower_photos", 224, 224, 4)
    #模型加载
    model = model_load(is_transfer=is_transfer)
    history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)
    if is_transfer:
        # model.evaluate(val_ds)
        model.save("models/mobilenet_flower.h5")
    else:
        model.save("models/cnn_flower.h5")
    show_loss_acc(history)


if __name__ == '__main__':
    train(epochs=10, is_transfer=True)
    train(epochs=4, is_transfer=False)
    # test()

