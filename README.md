# 代码说明

## 数据集

Latest EqualChange dataset (similar duplicate images replaced)
https://drive.google.com/drive/folders/1MgzE1ab5IbS_qn_8hRD5tlBs9h3H926y?usp=drive_link

THE PRS250 contains REAL, PAINTING and SKETCH domains，250 images per category
https://drive.google.com/drive/folders/1ve1RWwe8yx5Dv7rllkbGuJGSnxShpeJ1?usp=drive_link

Old EqualChange dataset (similar duplicate images not replaced)
https://drive.google.com/drive/folders/1iOIZWzEkkeBrj_MOrP1Zpnrk9FA3drYH?usp=drive_link

本代码共分四个部分，分别是基线方法，域适应方法，风格迁移，相同相似检测，其中前三个都用到了不同的库。

## 基线方法

主要文件在Train_Custom_Dataset-main文件夹，实现resnet18和resnet50的迁移学习基线测试。

具体使用和依托的库可查看：https://github.com/TommyZihao/Train_Custom_Dataset # @TommyZihao

将本文件夹移入其中替换相应文件，完成环境配置即可使用

本文件夹中代码为修改后的主要用于训练和测试的代码，训练测试代码在一起。其他评估，可视化等代码参看上述库中相应路径加下的文件。

## 域适应方法

主要文件在Transfer-Learning-Library-master文件夹，实现论文中各种域适应测试

具体使用和依托的库可查看：https://github.com/thuml/Transfer-Learning-Library # @thuml

将本文件夹移入其中替换相应文件，完成环境配置即可使用

本文件夹中代码为修改后的主要用于提供EqualChange数据集的配置文件和连续执行文件

@misc{jiang2022transferability,
   title={Transferability in Deep Learning: A Survey}, 
   author={Junguang Jiang and Yang Shu and Jianmin Wang and Mingsheng Long},
   year={2022},
   eprint={2201.05867},
   archivePrefix={arXiv},
   primaryClass={cs.LG}
}

@misc{tllib,
  author = {Junguang Jiang, Baixu Chen, Bo Fu, Mingsheng Long},
  title = {Transfer-Learning-library},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{![img](file:///C:\Users\Richard\AppData\Roaming\Tencent\QQTempSys\[5UQ[BL(6~BS2JV6W}N6[%S.png)https://github.com/thuml/Transfer-Learning-Library}},
}

## 风格迁移

主要文件在fast-neural-style-tensorflow-master文件夹，实现论文中图像风格迁移部分

具体使用和依托的库可查看：https://github.com/hzy46/fast-neural-style-tensorflow # @Zhiyuan He

将本文件夹移入其中替换相应文件，完成环境配置即可使用

本文件夹中代码为修改后的主要用于提供图片配置文件，连续生成文件，连续模型训练文件

## 相同相似检测

主要文件在fast-neural-style-tensorflow-master文件夹，实现论文中图像风格迁移部分

将本文件夹移入其中替换相应文件，完成环境配置即可使用

本文件夹包含检索相同相似图片，替换相同相似图片的代码


