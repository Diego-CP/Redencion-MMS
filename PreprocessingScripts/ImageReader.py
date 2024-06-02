import cv2

img_file = cv2.imread(r"C:\DATA_REDENCION\DeepGlobeDataset\data\ann_dir\train_test\311386_mask.png")

file = open('C:\DATA_REDENCION\ResultMatrix.txt', 'w')
for i in img_file:
    file.write(str(i))
file.close()