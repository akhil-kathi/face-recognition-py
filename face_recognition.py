from picamera import PiCamera
import face_recognition
from time import sleep
import cv2
cam= cv2.VideoCapture(0)

img1 = face_recognition.load_image_file('/home/pi/Desktop/Akhil.jpg')
img_landmarks = face_recognition.face_landmarks(img1)
img_encoding_1 =face_recognition.face_encodings(img1)[0]
face_locations = []
face_encodings = []

while True:
    val,img=cam.read()
    cv2.startWindowThread()
    cv2.namedWindow("abc")
    cv2.imshow("abc",img)
    cv2.waitKey()
      # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(x)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(x, face_locations)

    # Loop over each face found in the frame to see if it's someone we know.
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces([img_encoding_1], face_encoding)
        name = "<Unknown Person>"

        if match[0]:
            name = "Akhil"

        print("I see someone named {}!".format(name))

    sleep(10000)



