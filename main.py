import os
import cv2
import pickle
import face_recognition
import numpy as np
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://accesscontrolfacerecog-default-rtdb.firebaseio.com/",
    'storageBucket': "accesscontrolfacerecog.appspot.com"
})

bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

#Importando as imagens da pasta modes para uma lista
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# Carregando o Encode File
print("Carregando o arquivo de codificação ...")
file = open("EncodeFile.p", 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print("Arquivo de codificação carregado")


modeType = 0
contador = 0
id = -1
imgAluno = []

while True:
    success, img = cap.read()

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    if faceCurFrame:
        for encodeFace, faceLoc in zip (encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                print("Rosto conhecido detectado!")
                #print(studentIds[matchIndex])
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                id = studentIds[matchIndex]

                if contador == 0:
                    cvzone.putTextRect(imgBackground, "Carregando...", (275, 400))
                    cv2.imshow("Reconhecimento Facial", imgBackground)
                    cv2.waitKey(1)
                    contador = 1
                    modeType = 1

        if contador != 0:

            if contador == 1:
                # Get the Data
                studentInfo = db.reference(f'Alunos/{id}').get()
                print(studentInfo)

                # Get the image from the storage
                blob = bucket.get_blob(f'Images/{id}.png')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgAluno = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

                  # Update data of attendance
                datetimeObject = datetime.strptime(studentInfo['ultimoAcesso'],
                                                    '%d-%m-%Y %H:%M:%S')
                secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                print(secondsElapsed)
                if secondsElapsed > 30:
                    ref = db.reference(f'Alunos/{id}')
                    studentInfo['numeroAtendimentos'] += 1
                    ref.child('numeroAtendimentos').set(studentInfo['numeroAtendimentos'])
                    ref.child('ultimoAcesso').set(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
                else:
                    modeType = 3
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

            if modeType != 3:

                if 10 < contador < 20:
                    modeType = 2

                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

                if contador <= 10:

                    cv2.putText(imgBackground, str(studentInfo['numeroAtendimentos']), (861,125),cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)

                    #cv2.putText(imgBackground, str(studentInfo['matricula']), (1006,550),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 1)
                    cv2.putText(imgBackground, str(studentInfo['matricula']), (1006,493),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 1)

                    #cv2.putText(imgBackground, str(id), (1006,493),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 1)

                    #cv2.putText(imgBackground, str(studentInfo['curso']), (910,625),cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
                    cv2.putText(imgBackground, str(studentInfo['curso']), (980,550),cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255), 1)

                    #cv2.putText(imgBackground, str(studentInfo['anoIngresso']), (1125,625),cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)

                    (w, h), _ = cv2.getTextSize(studentInfo['nome'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset = (414 - w) // 2
                    cv2.putText(imgBackground, str(studentInfo['nome']), (808 + offset, 445),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)

                    imgAluno = cv2.resize(imgAluno, (216, 216))
                    imgBackground[175:175 + 216, 909:909 + 216] = imgAluno

                contador += 1
                    
                if contador >= 20:
                    contador = 0
                    modeType = 0
                    studentInfo = []
                    imgStudent = []
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
    else:
        modeType = 0
        contador = 0

    # cv2.imshow("Webcam", img)
    cv2.imshow("Reconhecimento Facial", imgBackground)
    cv2.waitKey(1)