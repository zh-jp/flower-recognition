# flower-recognition


基于Tensorflow花卉识别
[参考开源代码](https://github.com/cmFighting/Flower_tf2.3)

---

## How To Use

- 创建conda虚拟环境（首先你要去官网下载anaconda3）

  ```bash
  conda create -n yourenvname python=3.7
  ```
- 进入已经创建好的虚拟环境

  ```
  conda activate yourenvname
  ```
- 安装英伟达深度学习软件包（AMD显卡可以忽略）

  ```bash
  conda install cudatoolkit=10.1
  conda install cudnn=7.6
  ```
- 安装GPU版本的tensorflow

  ```bash
  pip install tensorflow-gpu==2.3
  ```
- 安装CPU版本的tensorflow（电脑无显卡的用这个）

  ```
  pip install tensorflow-cpu==2.3
  ```
- 安装 `streamlit`库

```bash
pip install streamlit
```

- 执行命令：

```bash
streamlit run .\webpage.py
```

打开可视化界面

## The Catalogue

- `.idea`: Pycharm配置文件
- `data`: 存放数据集
- `imgs`: 存放网页图片
- `utils`: 工具代码文件夹
- `train`: 深度学习相关代码
- `webpage.py`: Streamlit前端

