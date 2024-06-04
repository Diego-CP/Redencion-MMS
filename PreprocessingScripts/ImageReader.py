import cv2

img_file = cv2.imread(r"C:\TEC\Semestre8\Desarrollo\ActividadGerry\MMSeg\mmsegmentation\data\deepglobe\ann_dir\train\311386_mask.png")

file = open(r'C:\TEC\ResultMatrix.txt', 'w')
for i in img_file:
    file.write(str(i))
file.close()