# Dataset configuration files

import os
from typing import Optional
from .imagelist import ImageList
from ._util import download as download_data, check_exits


class EqualChange(ImageList):

    """`EqualChange <http://ai.bu.edu/M3SDA/#dataset>`_ (cleaned version, recommended)

    .. note:: In `root`, there will exist following files after downloading.
        ::
            real/
            painting/
            sketch/
            real-processing/
            painting-processing/

            real-cubist/
            real-denoised-starry/
            real-feathers/
            real-mosaic/
            real-scream/
            real-udnie/
            real-wave/
            image_list/
                real.txt
                ...
    """


    download_list = [
        # ("image_list", "image_list.zip", "https://cloud.tsinghua.edu.cn/f/bf0fe327e4b046eb89ba/?dl=1"),
        # ("real-processing", "real-processing.zip", "https://cloud.tsinghua.edu.cn/f/f0515164a4864220b98b/?dl=1"),
        # ("painting-processing", "painting-processing.zip", "https://cloud.tsinghua.edu.cn/f/98b19d5fc9884109a9cb/?dl=1"),
        # ("painting", "painting.zip", "https://cloud.tsinghua.edu.cn/f/11285ce9fbd34bb7b28c/?dl=1"),
        # ("real", "real.zip", "https://cloud.tsinghua.edu.cn/f/17a101842c564959b525/?dl=1"),
        # ("sketch", "sketch.zip", "https://cloud.tsinghua.edu.cn/f/b305add26e9d47349495/?dl=1"),
        # ("real-cubist", "real-cubist.zip", "https://cloud.tsinghua.edu.cn/f/bf0fe327e4b046eb89ba/?dl=1"),
        # ("real-denoised-starry", "real-denoised-starry.zip", "https://cloud.tsinghua.edu.cn/f/f0515164a4864220b98b/?dl=1"),
        # ("real-feathers", "real-feathers.zip", "https://cloud.tsinghua.edu.cn/f/98b19d5fc9884109a9cb/?dl=1"),
        # ("real-mosaic", "real-mosaic.zip", "https://cloud.tsinghua.edu.cn/f/11285ce9fbd34bb7b28c/?dl=1"),
        # ("real-scream", "real-scream.zip", "https://cloud.tsinghua.edu.cn/f/6faa9efb498b494abf66/?dl=1"),
        # ("real-udnie", "real-udnie.zip", "https://cloud.tsinghua.edu.cn/f/17a101842c564959b525/?dl=1"),
        # ("real", "real.zip", "https://cloud.tsinghua.edu.cn/f/17a101842c564959b525/?dl=1"),
        # ("real-wave", "real-wave.zip", "https://cloud.tsinghua.edu.cn/f/6faa9efb498b494abf66/?dl=1"),
    ]


    image_list = {

        "r": "real",
        "p": "painting",
        "s": "sketch",
        "rp": "real-processing",
        "pp": "painting-processing",

        "r_c": "real-cubist",
        "r_ds": "real-denoised-starry",
        "r_f": "real-feathers",
        "r_m": "real-mosaic",
        "r_s": "real-scream",
        "r_u": "real-udnie",
        "r_w": "real-wave",


    }


    CLASSES = ['The_Eiffel_Tower', 'The_Great_Wall_of_China', 'airplane', 'ant', 'anvil', 'apple', 'asparagus', 'axe', 'banana',
                 'barn', 'basketball', 'bat', 'bear', 'bicycle', 'blueberry', 'brain', 'bridge', 'butterfly', 'cake', 'camel',
                 'camera', 'campfire', 'candle', 'canoe', 'car', 'castle', 'cat', 'church', 'circle', 'clock', 'cloud', 'crab',
                 'cups', 'dog', 'dragon', 'drums', 'duck', 'elephant', 'envelope', 'firetruck', 'fish', 'flower', 'flying_saucer',
                 'frog', 'garden', 'guitar', 'harp', 'hat', 'hockey_puck', 'horse', 'hot_air_balloon', 'hourglass', 'kangaroo',
                 'lantern', 'leaf', 'light_bulb', 'lighthouse', 'lightning', 'lion', 'lobster', 'lollipop', 'map', 'microphone',
                 'monkey', 'moon', 'mountain', 'mouse', 'mushroom', 'ocean', 'octopus', 'onion', 'owl', 'panda', 'parrot', 'pear',
                 'penguin', 'piano', 'pig', 'rabbit', 'rain', 'rhinoceros', 'river', 'sailboat', 'saxophone', 'sheep', 'skateboard',
                 'skull', 'slippers', 'snail', 'snake', 'snowman', 'soccer_ball', 'spider', 'squirrel', 'stethoscope', 'strawberry',
                 'submarine', 'suitcase', 'sun', 'swan', 'tent', 'tiger', 'tornado', 'tractor', 'train', 'tree', 'triangle',
                 'trombone', 'truck', 'vase', 'violin', 'watermelon', 'windmill', 'yoga']

    def __init__(self, root: str, task: str, split: Optional[str] = 'train', download: Optional[float] = False, **kwargs):
        assert task in self.image_list
        assert split in ['train', 'test']
        data_list_file = os.path.join(root, "image_list", "{}_{}.txt".format(self.image_list[task], split))
        print("loading {}".format(data_list_file))

        if download:
            list(map(lambda args: download_data(root, *args), self.download_list))
        else:
            list(map(lambda args: check_exits(root, args[0]), self.download_list))

        super(EqualChange, self).__init__(root, EqualChange.CLASSES, data_list_file=data_list_file, **kwargs)

    @classmethod
    def domains(cls):
        return list(cls.image_list.keys())
