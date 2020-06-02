import cv2

# url = 'Test1.mp4'
url = 'Test2.mp4'
x = 0
hog = cv2.HOGDescriptor()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Supporting file
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

try:
    cap = cv2.VideoCapture(url)

except:
    print("Video not found")

while True:
    x = x + 1
    r, frame = cap.read()

    if r:
        frame = cv2.resize(frame, (550, 360))  # Downscale to improve frame rate
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)  # HOG needs a grayscale image
        rects, weights = hog.detectMultiScale(gray_frame)

        # Detecting motorcycle riders
        for i, (x, y, w, h) in enumerate(rects):
            if weights[i] < 0.8:
                continue
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
            crop_img = frame[y: y + h, x: x + w]  # Size of the cropped image varies along with frame
            crop_img = cv2.resize(crop_img, (300, 500))
            cv2.imshow("Streaming...!", frame)

            # Looking for helmet in the frame
            gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)  # HOG needs a grayscale image
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.3,
                minNeighbors=3,
                minSize=(30, 30)
            )
            for (x, y, w, h) in faces:
                detect = cv2.rectangle(crop_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # if detect is not None:
                    # cv2.imwrite("Detected_Img/face" + str(x) + ".jpg", crop_img)
            cv2.imshow("Detected_Img", crop_img) # Show dedicated window

    if cv2.waitKey(1) & 0xFF == ord("q"): # Break the execution
        break