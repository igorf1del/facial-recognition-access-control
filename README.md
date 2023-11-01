<!-- Título -->
<h1 align="center">Controle de Acesso de Alunos por Reconhecimento Facial</h1>

![background](https://github.com/igorf1del/teste/assets/85898252/0ef8dced-82f0-425b-8011-3681620ab859)

## Visão Geral

<p align="justify">
Este projeto implementa um sistema de controle de acesso para estudantes universitários por meio de reconhecimento facial. Ele é projetado para conceder ou negar o acesso a uma faculdade com base na identificação facial dos alunos. 
</p>

## Objetivos

O objetivo principal deste projeto é implementar um sistema de controle de acesso que utiliza o reconhecimento facial como método de autenticação. Alguns dos objetivos específicos incluem:

1. **Reconhecimento Facial Eficiente:** Desenvolver um sistema de reconhecimento facial preciso e rápido que funcione em tempo real e seja capaz de identificar alunos de forma confiável;

2. **Armazenamento de Dados Seguro:** Utilizar o Firebase para armazenar informações de alunos e imagens de maneira segura e escalável, garantindo que todos os dados estejam protegidos e disponíveis em tempo real;

3. **Registro de Acesso e Atualizações:** Manter um registro detalhado de cada acesso dos alunos, incluindo a data e hora do último acesso, e atualizar as informações no Firebase Realtime Database em tempo real;

4. **Interação com os Alunos:** Fornecer uma interface interativa que exiba informações sobre os alunos quando reconhecidos, incluindo nome, curso e matrícula;

5. **Facilidade de Uso:** Criar uma aplicação de fácil utilização, com modos de operação claros para refletir o status do sistema.

### Principais Recursos

- Reconhecimento facial em tempo real;
- Armazenamento seguro de informações de alunos e imagens no Firebase;
- Registros detalhados de acesso e atualizações em tempo real no Firebase Realtime Database;
- Interface interativa para exibir informações de alunos.

### Diretórios

A aplicação apresenta basicamente duas pastas:

  - **Images:** Armazena fotos de alunos hipotéticos que são enviadas para o banco de dados para fins de teste;
  - **Resources:** Guarda layouts de telas de status e a tela de fundo.

### Banco de Dados

<p align="justify">
  Para realizar testes de reconhecimento facial, foi preciso ter o banco de dados no Firebase devidamente configurado e populado com informações pessoais de alguns alunos hipotéticos. O banco de dados desempenha um papel central no funcionamento do sistema, pois contém não apenas as codificações faciais dos alunos, mas também detalhes relevantes, como nome, matrícula, curso, ano de ingresso, a última vez que acessaram as instalações da instituição e suas fotos.
</p>

### Classes:

<p align="justify">
  1. <b>Encode Generator:</b> Esta classe tem como objetivo gerar as codificações faciais das imagens dos alunos e armazená-las em um formato apropriado para uso posterior. Isso permite ao sistema comparar os rostos capturados em tempo real com os rostos já registrados, facilitando o reconhecimento dos alunos. As codificações são armazenadas no Firebase Cloud Storage;
</p>

<p align="justify">
  2. <b>AddDataToDatabase:</b> Essa classe é responsável por inserir os dados dos alunos no Firebase Realtime Database, permitindo que essas informações sejam armazenadas e recuperadas em tempo real;
</p>

<p align="justify">
  3. <b>Classe Main:</b> Nesta classe é onde o reconhecimento facial de fato acontece. O programa utiliza a biblioteca "face_recognition" para identificar as pessoas que se aproximam da câmera. Uma vez que um aluno  é reconhecido, suas informações pessoais são recuperadas do banco de dados e exibidas na tela. O programa verifica o tempo decorrido desde o último acesso do aluno e mantém um registro do número de vezes que um aluno é detectado pela câmera. A aplicação possui diferentes modos de operação que controlam o que é exibido na tela com base nas ações realizadas.
</p>

## Tecnologias Utilizadas

Para a implementação deste projeto foi necessário o uso de algumas tecnologias e bibliotecas fundamentais. Dentre as principais estão:

- **Python:** A linguagem de programação usada para desenvolver a lógica e as funcionalidades;

- **OpenCV (cv2):** Uma biblioteca amplamente utilizada para processamento de imagens e visão computacional, essencial para a captura de imagens e reconhecimento facial em tempo real;

- **Pickle:** Biblioteca Python que permite serializar e desserializar objetos, usada para armazenar as codificações faciais das imagens dos alunos em formato apropriado;

- **Face_Recognition:** Biblioteca de código aberto baseada em Python que fornece poderosas ferramentas para reconhecimento facial, simplificando o processo de identificação de faces em imagens e vídeos;

- **NumPy:** Essencial para cálculos numéricos em Python, amplamente utilizada para operações de matriz, como manipulação de imagens;

- **cvzone:** Responsável por estender as funcionalidades do OpenCV, permitindo a criação de interfaces gráficas interativas e adicionando recursos avançados;

- **Firebase Admin SDK:** Biblioteca oficial do Firebase que fornece acesso programático aos serviços do Firebase, incluindo o Firebase Realtime Database, Firebase Cloud Storage e autenticação;

- **Firebase Realtime Database:** Banco de dados NoSQL em tempo real hospedado na nuvem, usado para armazenar informações de alunos, como nome, matrícula, curso, ano de ingresso e outros dados;
  
- **Firebase Cloud Storage:** Serviço de armazenamento em nuvem do Firebase usado para armazenar imagens relacionadas aos alunos;

- **Datetime:** Biblioteca Python para manipulação de datas e horas, utilizada para registrar a data e hora do último acesso dos alunos.


## Instruções de uso

Siga estas etapas para usar o sistema de controle de acesso por reconhecimento facial:

1. **Configuração Inicial:**

   Certifique-se de ter todas as dependências e bibliotecas instaladas no seu ambiente Python.

2. **Baixando o Projeto:**

   - Clone este repositório para o seu repositório local usando o seguinte comando no seu terminal:

     ```
     git clone https://github.com/igorf1del/facial-recognition-access-control.git
     ```
     
3. **Populando o Banco de Dados:**

   - Utilize a classe `Encode Generator` para gerar as codificações faciais das imagens dos alunos e armazená-las no Firebase Cloud Storage. Isso é essencial para o reconhecimento facial em tempo real;

   - Use a classe `AddDataToDatabase` para inserir os dados dos alunos no Firebase Realtime Database. Isso inclui informações como nome, matrícula, curso, ano de ingresso e outros detalhes.

4. **Executando a Aplicação:**

   - Execute a classe `Main` para iniciar o reconhecimento facial em tempo real.

5. **Interagindo com o Sistema:**

   - Quando um aluno é reconhecido, suas informações pessoais são exibidas na tela, incluindo matrícula, curso, nome e número de atendimentos;

   - O sistema verifica o tempo decorrido desde o último acesso do aluno e atualiza as informações de data/hora no Firebase correspondentes ao último acesso;

   - A aplicação possui diferentes modos de operação que controlam o que é exibido na tela com base nas ações realizadas.

## Contribuições

Contribuições e feedbacks são bem-vindos! Sinta-se à vontade para abrir problemas, enviar solicitações de pull ou fornecer sugestões para aprimorar e expandir este projeto.
