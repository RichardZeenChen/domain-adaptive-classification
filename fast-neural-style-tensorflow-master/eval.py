# coding: utf-8
from __future__ import print_function
import tensorflow as tf
from preprocessing import preprocessing_factory
import reader
import model
import time
import os

tf.app.flags.DEFINE_string('loss_model', 'vgg_16', 'The name of the architecture to evaluate. '
                           'You can view all the support models in nets/nets_factory.py')
tf.app.flags.DEFINE_integer('image_size', 256, 'Image size to train.')
tf.app.flags.DEFINE_string("model_file", "models.ckpt", "")
tf.app.flags.DEFINE_string("image_file", "a.jpg", "")

FLAGS = tf.app.flags.FLAGS

def in_img(x):
    return x

def in_mod(y):
    return y

def save(z):
    return z
def main(_):
# def main(_):, in_mod


    # Get image's height and width.
    height = 0
    width = 0

    # FLAGS.image_file = 'content/ant/3.jpg'
    FLAGS.image_file = in_img(x)
    with open(FLAGS.image_file, 'rb') as img:
        with tf.Session().as_default() as sess:
            if FLAGS.image_file.lower().endswith('png'):
                image = sess.run(tf.image.decode_png(img.read()))
            else:
                image = sess.run(tf.image.decode_jpeg(img.read()))
            height = image.shape[0]
            width = image.shape[1]
    tf.logging.info('Image size: %dx%d' % (width, height))

    with tf.Graph().as_default():
        with tf.Session().as_default() as sess:

            # Read image data.
            image_preprocessing_fn, _ = preprocessing_factory.get_preprocessing(
                FLAGS.loss_model,
                is_training=False)
            image = reader.get_image(FLAGS.image_file, height, width, image_preprocessing_fn)

            # Add batch dimension
            image = tf.expand_dims(image, 0)

            generated = model.net(image, training=False)
            generated = tf.cast(generated, tf.uint8)

            # Remove batch dimension
            generated = tf.squeeze(generated, [0])

            # Restore model variables.
            saver = tf.train.Saver(tf.global_variables(), write_version=tf.train.SaverDef.V1)
            sess.run([tf.global_variables_initializer(), tf.local_variables_initializer()])
            # Use absolute path

            # FLAGS.model_file = 'models/mosaic.ckpt-done'
            FLAGS.model_file = in_mod(y)
            # in_mod = 'models/mosaic.ckpt-done'
            # FLAGS.model_file = in_mod
            FLAGS.model_file = os.path.abspath(FLAGS.model_file)

            saver.restore(sess, FLAGS.model_file)

            # Make sure 'generated' directory exists.
            # generated_file = 'generated/res4.jpg'
            generated_file = save(z)
            if os.path.exists('generated') is False:
                os.makedirs('generated')

            # Generate and write image data to file.
            with open(generated_file, 'wb') as img:
                start_time = time.time()
                img.write(sess.run(tf.image.encode_jpeg(generated)))
                end_time = time.time()
                tf.logging.info('Elapsed time: %fs' % (end_time - start_time))

                tf.logging.info('Done. Please check %s.' % generated_file)

#
# # if __name__ == '__main__':
# # path_in_img = 'models/'
# path_in_mod = 'models/'
#

##对一个域的数据进行所有风格迁移
##Perform all style migrations for data in a domain
# for q in os.listdir('models/'): # 遍历每个模型/Iterate through each model
#
#     path_in_img = 'content/R2/'
#
#     dataset_path = 'generated/'
#
#     mod_name = q[:-10] # 获取风格名/Get style name
#     # 每个风格创建一个，风格+数据集名文件夹/Create one per style, style + dataset name folder
#     os.mkdir(os.path.join(dataset_path, 'R2_' + mod_name)) 
#     dataset_name = 'R2_' + mod_name
#     #保存的路径为工程目录下，生成文件夹/风格+数据集名文件夹/
#     # The path to save is in the project directory, generate folder / style + dataset name folder /
#     path_save = 'generated/' + dataset_name + '/' 
#     # 遍历指定数据集下每个类/Iterate through each class under the specified dataset
#     for classes in os.listdir(path_in_img): 
#         mod_class = mod_name
#         # 创建与content数据集下下相同的类文件夹/Create the same class folder as under the content dataset
#         os.mkdir(os.path.join(path_save, classes)) 
#         path_in_img_clas = path_in_img + classes + '/'
#         count = 0
#         for per_img in os.listdir(path_in_img_clas): # 遍历每张图/Iterate over each graph
#
#             count = count + 1
#             # 指定内容图片访问路径/Specify the path to access content images
#             x = path_in_img_clas + '/' + per_img 
#             in_img(x)
#             # 指定风格模型文件访问路径/Specify the path to access the style model file
#             y = path_in_mod + q 
#             in_mod(y)
#             # z = path_save + 'ant' + str(count) + '.jpg'
#             # 指定生成的风格+内容图片的保存路径及名称/Specify the save path and name of the generated style + content images
#             # if count < 10: 
#             #     z = path_save + classes + '/' + mod_class + '_00000' + str(count) + '.jpg'
#             # elif count < 100:
#             #     z = path_save + classes + '/' + mod_class + '_0000' + str(count) + '.jpg'
#             # elif count < 1000:
#             #     z = path_save + classes + '/' + mod_class + '_000' + str(count) + '.jpg'
#             z = path_save + classes + '/' + mod_class + '_' + per_img
#             save(z)
#             main(0)
#tf.logging.set_verbosity(tf.logging.INFO)
# tf.app.run()

#
# #对一个类的数据进行一种风格迁移/One style migration for data of a class
# count = 0
# path_in_mod = 'models/wave_test.ckpt-done'
# path_in_img = 'content/perfirst/'
# dataset_path = 'generated/'
# classe = 'perfirst'
# mod_name = 'wave_test' # 获取风格名/Get style name
##保存的路径为工程目录下，生成文件夹/风格+数据集名文件夹/
##The path to save is in the project directory, generate folder / style + dataset name folder /
# path_save = 'generated/'  
#
# os.mkdir(os.path.join(path_save, classe + '-' + mod_name))
# for per_img in os.listdir(path_in_img):  # 遍历每张图/Iterate over each graph
#
#     count = count + 1
#     # 指定内容图片访问路径/Specify the path to access content images
#     x = path_in_img + '/' + per_img  
#     in_img(x)
#     y = path_in_mod # 指定风格模型文件访问路径/Specify the path to access the style model file
#     in_mod(y)
#
#     z = path_save + classe+ '-' + mod_name + '/' + mod_name + per_img# + mod_name + '_'
#     save(z)
#     main(0)
#
# tf.logging.set_verbosity(tf.logging.INFO)
# tf.app.run()


# 对个类的数据进行个生成的风格迁移/Generated style migrations for individual classes of data
path_in_mod = 'models/CANDY10/'
for q in os.listdir('models/CANDY10/'): # 遍历每个模型/Iterate through each model

    path_in_img = 'content/perfirst/'

    dataset_path = 'generated/'

    mod_name = q[:-10] # 获取风格名/Get style name
    # 获取风格类型名/Get style type name
    b = mod_name.find('_')
    c = list(mod_name)
    d = c.pop(b)
    e = ''
    for i in c:
        e = e + i
    imgclass_name = e + '%'
    # 每个风格创建一个，风格+数据集名文件夹/Create one per style, style + dataset name folder
    os.mkdir(os.path.join(dataset_path, 'perfirst_' + mod_name)) 
    dataset_name = 'perfirst_' + mod_name
    #保存的路径为工程目录下，生成文件夹/风格+数据集名文件夹/
    # The path to save is in the project directory, generate folder / style + dataset name folder /
    path_save = 'generated/' + dataset_name + '/' 
    count = 0.
    # 遍历指定数据集下每个类
    # Iterate over each class under the specified dataset
    for per_img in os.listdir(path_in_img): 
        # mod_class = mod_name
        ## 创建与content数据集下下相同的类文件夹/Create the same class folder as under the content dataset
        # os.mkdir(os.path.join(path_save, classes))
        # path_in_img_clas = path_in_img + classes + '/'

        # for per_img in os.listdir(path_in_img_clas): # 遍历每张图/Iterate over each graph

            count = count + 1
            # 指定内容图片访问路径/Specify the path to access content images
            x = path_in_img + '/' + per_img 
            in_img(x)
            # 指定风格模型文件访问路径/Specify the path to access the style model file
            y = path_in_mod + q 
            in_mod(y)
            # z = path_save + 'ant' + str(count) + '.jpg'
            # if count < 10: # 指定生成的风格+内容图片的保存路径及名称
            #     z = path_save + classes + '/' + mod_class + '_00000' + str(count) + '.jpg'
            # elif count < 100:
            #     z = path_save + classes + '/' + mod_class + '_0000' + str(count) + '.jpg'
            # elif count < 1000:
            #     z = path_save + classes + '/' + mod_class + '_000' + str(count) + '.jpg'
            # z = path_save + classes + '/' + mod_class + '_' + per_img
            z = path_save + '/' + imgclass_name + '_' + per_img
            save(z)
            main(0)
tf.logging.set_verbosity(tf.logging.INFO)
tf.app.run()



