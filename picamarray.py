import picamera
import picamera.array
import face_recognition 

face_locations = []
face_encodings = []

me = fr.load_image_file("/home/pi/Desktop/Akhil.jpg")
face_encode = fr.face_encodings(me)[0]

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as output:
       pixel=  camera.start_preview()
       while True:
           face_locations=face_recognition.face_locations(pixel)
           face_encodings=face_recognition.face_encodings(pixel,face_locations)
           for face_encoding in face_encodings:
               match=fr.compare_faces([face_encode],face_encoding)
               name=None
               if match[0]:
                   name="Akhil"
               else:
                   print("I don't know")
           sleep(1000)

        



