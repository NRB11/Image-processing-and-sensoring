import cv2 
import numpy as np

img = cv2.imread("miniproject/pictures/1.jpg")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

Square1 = img2[0:100,0:100]; Square2 = img2[0:100,100:200]; Square3 = img2[0:100,200:300]; Square4 = img2[0:100,300:400]; Square5 = img2[0:100,400:500]
Square6 = img2[100:200,0:100]; Square7 = img2[100:200,100:200]; Square8 = img2[100:200,200:300]; Square9 = img2[100:200,300:400]; Square10 = img2[100:200,400:500]
Square11 = img2[200:300,0:100]; Square12 = img2[200:300,100:200]; Square13 = img2[200:300,200:300]; Square14 = img2[200:300,300:400]; Square15 = img2[200:300,400:500]
Square16 = img2[300:400,0:100]; Square17 = img2[300:400,100:200]; Square18 = img2[300:400,200:300]; Square19 = img2[300:400,300:400]; Square20 = img2[300:400,400:500]
Square21 = img2[400:500,0:100]; Square22 = img2[400:500,100:200]; Square23 = img2[400:500,200:300]; Square24 = img2[400:500,300:400]; Square25 = img2[400:500,400:500]

Average1 = np.average(Square1,axis=0); colorAverage1 = np.average(Average1,axis=0); print('Average 1 =',colorAverage1[0])
Average2 = np.average(Square2,axis=0); colorAverage2 = np.average(Average2,axis=0); print('Average 2 =',colorAverage2[0])
Average3 = np.average(Square3,axis=0); colorAverage3 = np.average(Average3,axis=0); print('Average 3 =',colorAverage3[0])
Average4 = np.average(Square4,axis=0); colorAverage4 = np.average(Average4,axis=0); print('Average 4 =',colorAverage4[0])
Average5 = np.average(Square5,axis=0); colorAverage5 = np.average(Average5,axis=0); print('Average 5 =',colorAverage5[0])
Average6 = np.average(Square6,axis=0); colorAverage6 = np.average(Average6,axis=0); print('Average 6 =',colorAverage6[0])
Average7 = np.average(Square7,axis=0); colorAverage7 = np.average(Average7,axis=0); print('Average 7 =',colorAverage7[0])
Average8 = np.average(Square8,axis=0); colorAverage8 = np.average(Average8,axis=0); print('Average 8 =',colorAverage8[0])
Average9 = np.average(Square9,axis=0); colorAverage9 = np.average(Average9,axis=0); print('Average 9 =',colorAverage9[0])
Average10 = np.average(Square10,axis=0); colorAverage10 = np.average(Average10,axis=0); print('Average 10 =',colorAverage10[0])
Average11 = np.average(Square11,axis=0); colorAverage11 = np.average(Average11,axis=0); print('Average 11 =',colorAverage11[0])
Average12 = np.average(Square12,axis=0); colorAverage12 = np.average(Average12,axis=0); print('Average 12 =',colorAverage12[0])
Average13 = np.average(Square13,axis=0); colorAverage13 = np.average(Average13,axis=0); print('Average 13 =',colorAverage13[0])
Average14 = np.average(Square14,axis=0); colorAverage14 = np.average(Average14,axis=0); print('Average 14 =',colorAverage14[0])
Average15 = np.average(Square15,axis=0); colorAverage15 = np.average(Average15,axis=0); print('Average 15 =',colorAverage15[0])
Average16 = np.average(Square16,axis=0); colorAverage16 = np.average(Average16,axis=0); print('Average 16 =',colorAverage16[0])
Average17 = np.average(Square17,axis=0); colorAverage17 = np.average(Average17,axis=0); print('Average 17 =',colorAverage17[0])
Average18 = np.average(Square18,axis=0); colorAverage18 = np.average(Average18,axis=0); print('Average 18 =',colorAverage18[0])
Average19 = np.average(Square19,axis=0); colorAverage19 = np.average(Average19,axis=0); print('Average 19 =',colorAverage19[0])
Average20 = np.average(Square20,axis=0); colorAverage20 = np.average(Average20,axis=0); print('Average 20 =',colorAverage20[0])
Average21 = np.average(Square21,axis=0); colorAverage21 = np.average(Average21,axis=0); print('Average 21 =',colorAverage21[0])
Average22 = np.average(Square22,axis=0); colorAverage22 = np.average(Average22,axis=0); print('Average 22 =',colorAverage22[0])
Average23 = np.average(Square23,axis=0); colorAverage23 = np.average(Average23,axis=0); print('Average 23 =',colorAverage23[0])
Average24 = np.average(Square24,axis=0); colorAverage24 = np.average(Average24,axis=0); print('Average 24 =',colorAverage24[0])
Average25 = np.average(Square25,axis=0); colorAverage25 = np.average(Average25,axis=0); print('Average 25 =',colorAverage25[0])

cv2.imshow('max',img2)
cv2.waitKey(0)
