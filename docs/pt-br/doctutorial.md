👨‍💻 Doctutorial - Português 👩‍💻

Bem-vindo ao BioBytes!
🔬 Introdução
O BioBytes é um projeto empolgante que combina os campos da biologia, genética e programação. Neste tutorial, iremos guiá-lo através do processo de instalação e configuração para começar com o BioBytes. Seja você um iniciante ou proveniente de uma área científica diferente, estamos aqui para ajudar! Vamos começar! 🌊

Passo 1: Instalando e Configurando o Ambiente
Clonar o Repositório

Abra o seu terminal ou prompt de comando.
Digite o seguinte comando para clonar o repositório:
bash
Copy code
git clone https://github.com/ulissesflores/BioBytes.git
Pressione Enter e aguarde o download do repositório para a sua máquina local.
Usando o Docker (Recomendado)

Instale o Docker no seu computador seguindo as instruções do site oficial do Docker: https://www.docker.com/get-started.
Após instalar o Docker, abra o terminal ou prompt de comando e navegue até o diretório do projeto.
Execute o seguinte comando para construir a imagem Docker:
Copy code
docker build -t biobytes .
Passo 2: Configurando o Ambiente
Ambiente Virtual (Opcional)

Se você preferir não utilizar o Docker, recomendamos criar um ambiente virtual para isolar as dependências do projeto.
Navegue até o diretório do projeto no seu terminal ou prompt de comando.
Execute os seguintes comandos para configurar o ambiente virtual:
bash
Copy code
python -m venv env
source env/bin/activate    # Para Linux/Mac
env\Scripts\activate       # Para Windows
Instalando as Dependências

Com o ambiente virtual ativado ou o Docker configurado, execute o seguinte comando para instalar as dependências do projeto:
Copy code
pip install -r requirements.txt
Passo 3: Executando o BioBytes
Iniciando a Aplicação

Se você estiver usando o Docker, execute o seguinte comando para iniciar o BioBytes:

arduino
Copy code
docker run -p 8000:8000 biobytes
Abra o seu navegador web e acesse http://localhost:8000 para acessar o BioBytes.

Se você não estiver usando o Docker, navegue até o diretório do projeto no seu terminal ou prompt de comando e execute o seguinte comando:

Copy code
python manage.py runserver
Abra o seu navegador web e visite http://localhost:8000 para acessar o BioBytes.

Explorando o BioBytes

Assim que a aplicação estiver em execução, você pode navegar pelas diferentes funcionalidades e seções.
🧬 Analise dados genéticos, 🧪 realize experimentos ou 🌱 simule processos biológicos. As possibilidades são infinitas!
Parabéns! 🎉 Você instalou e configurou o BioBytes com sucesso. Sinta-se à vontade para explorar, experimentar e contribuir para este projeto fascinante!