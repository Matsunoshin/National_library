import glob
import os

data_list = glob.glob('/Users/matsudashinichi/PycharmProjects/National_library/dataset/train_annotations/*.json')
path_w = '/Users/matsudashinichi/PycharmProjects/National_library/koten_train/ImageSets/Main/train.txt'

with open(path_w, mode='w') as f:
    f.write('')
    f.close()

for data in data_list:
    basename_without_ext = os.path.splitext(os.path.basename(data))[0]
    print(basename_without_ext)
    with open(path_w, mode='a') as f:
        f.write(basename_without_ext + '\n')
    f.close()

