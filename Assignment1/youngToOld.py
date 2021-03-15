import cv2

if __name__=='__main__':
    img_1 = cv2.imread("imgs/young.jpg")
    img_2 = cv2.imread("imgs/old.jpg")
    print(img_1.shape)
    print(img_2.shape)


    X,Y,_ = img_1.shape
    N = 20
    Output_Path = 'outputs/'
    for t in range(N):
        factor = t/N
        img_new = (1.0 - factor) * img_1 + factor * img_2    
        cv2.imwrite(Output_Path + 'img_new_' + str(t) + '.jpg' , img_new )