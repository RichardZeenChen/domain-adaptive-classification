##training model

import os

# os.system('cd COCO/train2014')
# os.system('ls')
# os.system('ln -s COCO_10/train2014 train2014')
# os.system('ls')
# os.system('rm train2014')
# os.system('ls')
#

##训练模型/training model

# 训练COCO_10的candy和wave模型/Training COCO_10's candy and wave models
os.system('ln -s COCO_10/train2014 train2014')
os.system('python train.py -c conf/candy_10.yml')
# os.system('tensorboard --logdir models/candy_10/')
os.system('rm train2014')
# os.system('ln -s COCO_10/train2014 train2014')
# os.system('python train.py -c conf/wave_10.yml')
# # os.system('tensorboard --logdir models/wave_10/')
# os.system('rm train2014')

# # 训练COCO_30的candy和wave模型/Training COCO_30's candy and wave models
# os.system('ln -s COCO_30/train2014 train2014')
# os.system('python train.py -c conf/candy_30.yml')
# # os.system('tensorboard --logdir models/candy_30/')
# os.system('rm train2014')
# os.system('ln -s COCO_30/train2014 train2014')
# os.system('python train.py -c conf/wave_30.yml')
# # os.system('tensorboard --logdir models/wave/')
# os.system('rm train2014')

# 训练COCO_50的candy和wave模型/Training COCO_50's candy and wave models
# os.system('ln -s COCO_50/train2014 train2014')
# os.system('python train.py -c conf/candy_50.yml')
# # os.system('tensorboard --logdir models/candy_50')
# os.system('rm train2014')
# os.system('ln -s COCO_50/train2014 train2014')
# os.system('python train.py -c conf/wave_50.yml')
# # os.system('tensorboard --logdir models/candy_50')
# os.system('rm train2014')

# 训练COCO_80的candy和wave模型/Training COCO_80's candy and wave models
# os.system('ln -s COCO_80/train2014 train2014')
# os.system('python train.py -c conf/candy_80.yml')
# # os.system('tensorboard --logdir models/candy_50')
# os.system('rm train2014')
# os.system('ln -s COCO_80/train2014 train2014')
# os.system('python train.py -c conf/wave_80.yml')
# # os.system('tensorboard --logdir models/candy_50')
# os.system('rm train2014')

# # 训练COCO的candy和wave模型/Training COCO's candy and wave models
# os.system('ln -s COCO/train2014 train2014')
# os.system('python train.py -c conf/candy.yml')
# # os.system('tensorboard --logdir models/candy_50')
# os.system('rm train2014')
# os.system('ln -s CO/train2014 train2014')
# os.system('python train.py -c conf/wave.yml')
# # os.system('tensorboard --logdir models/candy_50')
# os.system('rm train2014')

# #训练COCO_100的candy和wave模型/Training COCO_100's candy and wave models
# os.system('ln -s COCO_100/train2014 train2014')
# os.system('python train.py -c conf/candy_100.yml')
# # os.system('tensorboard --logdir models/candy_50')
# os.system('rm train2014')
# os.system('ln -s COCO_100/train2014 train2014')
# os.system('python train.py -c conf/wave_100.yml')
# # os.system('tensorboard --logdir models/candy_50')
# os.system('rm train2014')

#测试/test item
# os.system('ln -s COCO测试/train2014 train2014')
# os.system('python train.py -c conf/wave_test.yml')
# # os.system('tensorboard --logdir models/wave/')
# os.system('rm train2014')



