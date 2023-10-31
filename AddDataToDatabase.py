import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://accesscontrolfacerecog-default-rtdb.firebaseio.com/"
})

ref = db.reference('Alunos')

data = {

    "852741":
        {
            "nome": "Emily Blunt",
            "matricula": 202010103,
            "curso": "Direito",
            "anoIngresso": "2020.1",
            "ultimoAcesso": "30-08-2023 07:58:05",
            "numeroAtendimentos": 0

        },


    "963852":
        {
            "nome": "Elon Musk",
            "matricula": 1813080009,
            "curso": "Engenharia Civil",
            "anoIngresso": "2019.2",
            "ultimoAcesso": "28-08-2023 18:27:15",
            "numeroAtendimentos": 0

        },
        

    "333":
        {
            "nome": "Scarlett Johansson",
            "matricula": 3333333333,
            "curso": "Enfermagem",
            "anoIngresso": "2020.2",
            "ultimoAcesso": "02-09-2023 18:28:20",
            "numeroAtendimentos": 0

        },

    "222":
        {
            "nome": "Bill Gates",
            "matricula": 2222222222,
            "curso": "Sistemas de Informação",
            "anoIngresso": "2020.2",
            "ultimoAcesso": "02-09-2023 18:28:20",
            "numeroAtendimentos": 0

        }
    
}

for key,value in data.items():
    ref.child(key).set(value)
print("Dados enviados para o BD!")