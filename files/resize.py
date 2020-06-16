import cv2
imgs = ['DiRS.png', 'Million-AID.png', 'Paper.png', 'PPT.png']
# imgs = ['DiRS.png']
height = 400
for img in imgs:
    print(img)
    a = cv2.imread(img)
    h, w, c = a.shape
    x = cv2.resize(a, (int(w * height / h), height))
    # x = cv2.resize(a, (800, height))
    print(x.shape)
    cv2.imwrite(img.split(".")[0] + "-Head.png", x)
