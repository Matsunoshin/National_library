import numpy as np
import cv2
import ocv_func as ocv

class ocv_train_func:
    def __init__(self, img_no=np.zeros(9)):
        self.img_no = img_no

    def trimming(self, filename, labels):
        # 画像とラベルを受け取って画像を切り出し、学習データとして割り振る
        img = cv2.imread(filename, 1)
        for label in labels:
            save_img = img[label['box2d']['y1']:label['box2d']['y2'],
                           label['box2d']['x1']:label['box2d']['x2']]
            category_no = int(label['category'][0])
            self.img_no[category_no - 1] += 1

            cv2.imwrite('dataset/trimming_data/' + str(label['category']) + '/img_' +
                        str('{:.0f}'.format(self.img_no[category_no - 1])) + '.jpg', save_img)

            img = ocv.resize(img)


            # try:
            #     f = open("sample2.txt")
            #     txt = f.read()
            #     f.close()
            #     print(txt)
            # except FileNotFoundError as err:
            #     print("ファイルが存在しないため、読み込めませんでした。")
            # except Exception as other:
            #     print("ファイルが読み込めませんでした。")

    def resize(self, img):
        h, w, c = img.shape
        longest_edge = max(h, w)
        top = 0
        bottom = 0
        left = 0
        right = 0
        if h < longest_edge:
            diff_h = longest_edge - h
            top = diff_h // 2
            bottom = diff_h - top
        elif w < longest_edge:
            diff_w = longest_edge - w
            left = diff_w // 2
            right = diff_w - left
        else:
            pass

        img = cv2.copyMakeBorder(img, top, bottom, left, right,
                                 cv2.BORDER_CONSTANT, value=[0, 0, 0])

        img = cv2.resize(img, dsize=(28, 28))

        return img