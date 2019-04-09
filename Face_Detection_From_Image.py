import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# eye_casecade = cv2.CascadeClassifier("haarcascade_eye.xml")
#smile_casecade = cv2.CascadeClassifier("haarcascade_smile.xml")


img = cv2.imread("cat.jpg")

gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

faces =face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,
                                      minNeighbors=5)

#smile =smile_casecade.detectMultiScale(gray_img,scaleFactor=1.05,
#                                   minNeighbors=100)

# eye =eye_casecade.detectMultiScale(gray_img,scaleFactor=1.05,
#                                      minNeighbors=52)

# for x,y,w,h in faces:
#     img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# resized = cv2.resize(img,(int(img.shape[1]*1),int(img.shape[0]*1)))


# for x,y,w,h in eye:
#     img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# resized = cv2.resize(img,(int(img.shape[1]*1),int(img.shape[0]*1)))

for x,y,w,h in faces:
     img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
resized = cv2.resize(img,(int(img.shape[1]*1),int(img.shape[0]*1)))


cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()