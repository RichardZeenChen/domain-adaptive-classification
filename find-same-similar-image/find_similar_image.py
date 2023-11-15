import os
import cv2
import shutil
from PIL import Image
import csv


class Tool:
    # copy same file
    def process3(self, path):
        domains = os.listdir(path)
        abs_domain_list = []
        for domain in domains:
            if os.path.isdir(path + domain):
                print(path + domain + '/')
                abs_domain_list.append(path + domain + '/')
        for abs_domain in abs_domain_list:
            dir_list = os.listdir(abs_domain)
            for dir in dir_list:
                abs_dir = abs_domain + dir + '/'
                file_list = os.listdir(abs_dir)
                file_property_list = []
                for file in file_list:
                    abs_file = abs_dir + file
                    size = os.path.getsize(abs_file)
                    img = cv2.imread(abs_file)
                    h, w = 0, 0
                    if img is None:
                        # print(abs_file)
                        img = Image.open(abs_file)
                        w, h = img.size
                        file_property_list.append((abs_file, w, h, size))
                        continue
                    h, w, c = img.shape
                    file_property_list.append((abs_file, w, h, size))

                same_list = list()
                ids = [0] * len(file_property_list)
                k = 1
                m = 0

                for i in range(len(file_property_list)):
                    flag = False
                    for j in range(i + 1, len(file_property_list)):
                        if ids[i] != 1 and ids[j] != 1 and file_property_list[i][1:3] == file_property_list[j][1:3] and \
                                file_property_list[i][3] == file_property_list[j][3]:
                            flag = True
                            # add prefix
                            dir, file = os.path.split(file_property_list[j][0])
                            abs_file = dir + f'/{k:0>3}' + file
                            same_list.append(abs_file)
                            ids[j] = 1
                            m += 1
                    if flag:
                        dir, file = os.path.split(file_property_list[i][0])
                        abs_file = dir + f'/{k:0>3}' + file
                        same_list.append(abs_file)
                        ids[i] = 1
                        k += 1
                if same_list != []:
                    print(dir.split('/')[-1], m, len(same_list), sep='\t')  # class,same,all
                    copy_file(same_list)
            print('=' * 20)

    # find same and similar image
    def process4(self, path):
        domains = os.listdir(path)
        abs_domain_list = []
        for domain in domains:
            if os.path.isdir(path + domain):
                print(path + domain + '/')
                abs_domain_list.append(path + domain + '/')
        for abs_domain in abs_domain_list:
            dir_list = os.listdir(abs_domain)
            f = open(abs_domain.split('/')[-2] + '.csv', 'w', newline='')
            writer = csv.writer(f)
            writer.writerow(['class', 'same', 'similar', 'rest'])
            for dir in dir_list:
                abs_dir = abs_domain + dir + '/'
                file_list = os.listdir(abs_dir)
                file_property_list = []
                for file in file_list:
                    abs_file = abs_dir + file
                    size = os.path.getsize(abs_file)
                    img = cv2.imread(abs_file)
                    h, w = 0, 0
                    if img is None:
                        # print(abs_file)
                        img = Image.open(abs_file)
                        w, h = img.size
                        file_property_list.append((abs_file, w, h, size))
                        continue
                    h, w, c = img.shape
                    file_property_list.append((abs_file, w, h, size))

                same_list = list()
                ids = [0] * len(file_property_list)
                k = 1  # prefix
                m = 0
                for i in range(len(file_property_list)):
                    flag = False
                    for j in range(i + 1, len(file_property_list)):
                        if ids[i] != 1 and ids[j] != 1 and file_property_list[i][1:3] == file_property_list[j][1:3] and \
                                file_property_list[i][3] == file_property_list[j][3]:
                            flag = True
                            # add prefix
                            dir, file = os.path.split(file_property_list[j][0])
                            abs_file = dir + f'/{k:0>3}' + file
                            same_list.append(abs_file)
                            ids[j] = 1
                            m += 1

                    if flag:
                        dir, file = os.path.split(file_property_list[i][0])
                        abs_file = dir + f'/{k:0>3}' + file
                        same_list.append(abs_file)
                        ids[i] = 1
                        k += 1
                        m += 1
                # copy file
                # if same_list!=[]:
                #     copy_file(same_list)

                similar_list = list()  # 相似列表
                ids = [0] * len(file_property_list)  # 辅助数组，记录是否已经加入重复列表
                k = 1  # prefix
                n = 0  # without base
                for i in range(len(file_property_list)):
                    flag = False
                    for j in range(i + 1, len(file_property_list)):
                        diff = abs(file_property_list[i][3] - file_property_list[j][3])
                        if ids[i] != 1 and ids[j] != 1 and file_property_list[i][1:3] == file_property_list[j][
                                                                                         1:3] and 0 < diff < 2000:
                            flag = True
                            # add prefix
                            dir, file = os.path.split(file_property_list[j][0])
                            abs_file = dir + f'/{k:0>3}' + file
                            similar_list.append(abs_file)
                            ids[j] = 1
                            n += 1

                    if flag:
                        dir, file = os.path.split(file_property_list[i][0])
                        abs_file = dir + f'/{k:0>3}' + file
                        similar_list.append(abs_file)
                        ids[i] = 1
                        k += 1
                        n += 1  # add base item
                # copy file
                if similar_list != []:
                    copy_file(similar_list)
                print(dir.split('/')[-1], m, n, sep='\t')
                writer.writerow([dir.split('/')[-1], m, n])
            f.close()
            print('=' * 20)


def copy_file(same_list: list):
    flag = True
    for sl in same_list:
        dirt = ''
        dir, file = os.path.split(sl)
        dirt = dir[3:]  # remove Windows disk symbol
        if not os.path.exists(dirt):
            os.makedirs(dirt)
        # 拷贝文件
        abs_file = dir + '/' + file[3:]  # remove prefix
        dst = dirt + '/' + file
        shutil.copy(abs_file, dst)


# move replaced image to origin document
def move_same_image(path):
    for root, dirs, files in os.walk(path):
        if files != []:
            for f in files:
                fdst = f[3:]  # remove prefix
                s = root.replace('\\', '/')
                d = s.replace('(3)', '')
                # print(s+'/'+f)
                # print(d+'/'+fdst)
                shutil.copy(s + '/' + f, d + '/' + fdst)
    print('work done!')


def move_similar_image(path):
    for root, dirs, files in os.walk(path):
        if files != []:
            for f in files:
                fdst = f[3:]  # remove prefix
                s = root.replace('\\', '/')
                d = s.replace('(2)', '')
                # print(s+'/'+f)
                # print(d+'/'+fdst)
                shutil.copy(s + '/' + f, d + '/' + fdst)
    print('work done!')


if __name__ == '__main__':
    # move_same_image('D:/EC/PRS250(3)/')
    # move_similar_image('D:/EC/PRS250(2)/')
    t = Tool()
    t.process3('D:/EC/PRS250/')  # catution: add '/'
    # t.process4('D:/EC/PRS250/')
    # t.process4('D:/EC/OfficeHome/')
    # t.process4('D:/EC/DomainNet/')
    # print('work done',1)
