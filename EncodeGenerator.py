import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://accesscontrolfacerecog-default-rtdb.firebaseio.com/",
    'storageBucket': "accesscontrolfacerecog.appspot.com"
})

caminhoDaPasta = 'Images'
pathList = os.listdir(caminhoDaPasta)
imgList = []
alunosId = []

# Envio das imagens dos alunos para o banco de dados
for path in pathList:
    imgList.append(cv2.imread(os.path.join(caminhoDaPasta, path)))
    alunosId.append(os.path.splitext(path)[0])

    fileName = f'{caminhoDaPasta}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print("Imagens enviadas para o BD!")
print(alunosId)

def findEncodings(imagesList):

    encodeList = []

    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Codificação iniciada")
encodeListKnow = findEncodings(imgList)
encodeListKnowWithIds = [encodeListKnow, alunosId]
print("Codificação concluída")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnowWithIds, file)
file.close()
print("Arquivo salvo!")