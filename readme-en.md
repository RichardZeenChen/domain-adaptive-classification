# Code Description

## Dataset

Latest EqualChange dataset (similar duplicate images replaced)
https://drive.google.com/drive/folders/1MgzE1ab5IbS_qn_8hRD5tlBs9h3H926y?usp=drive_link

THE PRS250 contains REAL, PAINTING and SKETCH domains，250 images per category
https://drive.google.com/drive/folders/1ve1RWwe8yx5Dv7rllkbGuJGSnxShpeJ1?usp=drive_link

Old EqualChange dataset (similar duplicate images not replaced)
https://drive.google.com/drive/folders/1iOIZWzEkkeBrj_MOrP1Zpnrk9FA3drYH?usp=drive_link

This code is divided into four parts, namely baseline method, domain adaptation method, style migration, and same-similarity detection, the first three of which use different libraries.

## Baseline method

The main files are in the Train_Custom_Dataset-main folder, which implements the migration learning baseline test for resnet18 and resnet50.

The specific libraries used and relied upon can be viewed at: https://github.com/TommyZihao/Train_Custom_Dataset # @TommyZihao

Move this folder into it and replace the corresponding files to complete the environment configuration.

The code in this folder is the modified code mainly used for training and testing, and the training and testing code is together. For other evaluation, visualisation and other codes, please refer to the files under the corresponding paths in the above libraries.

## Domain Adaptation Methods

The main files are in the Transfer-Learning-Library-master folder, which realise the various domain adaptation tests in the paper.

The specific libraries used and relied upon can be found at: https://github.com/thuml/Transfer-Learning-Library # @thuml

Move this folder into it and replace the corresponding files, complete the environment configuration can be used!

The code in this folder is the modified configuration file and sequential execution file mainly used to provide the EqualChange dataset.

## Style Migration

The main files are in the fast-neural-style-tensorflow-master folder, implementing the image style migration part of the paper.

The specific libraries used and relied upon can be found at: https://github.com/hzy46/fast-neural-style-tensorflow # @Zhiyuan He

Move this folder into it and replace the corresponding files, complete the environment configuration and then you can use it.

The code in this folder is modified to provide image configuration files, continuous generation files and continuous model training files.

## Similarity detection

The main files are in the fast-neural-style-tensorflow-master folder, which implements the image style migration part of the paper.

Move this folder into it and replace the corresponding files, complete the environment configuration and you can use it.

This folder contains the code for retrieving and replacing similar images.

