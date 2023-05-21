# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster
# Use uma imagem oficial do Python como imagem base

# Set the working directory in the container
WORKDIR /app
# Defina o diretório de trabalho no contêiner

# Add metadata to the image
LABEL maintainer="Ulisses Flores <c.ulisses@gmail.com>"
LABEL version="1.0"
LABEL description="This is BioBytes, a Python-based life simulator"
# Adicione metadados à imagem

# Copy the current directory contents into the container at /app
COPY . /app
# Copie o conteúdo do diretório atual para o contêiner em /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Instale os pacotes necessários especificados em requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80
# Deixe a porta 80 disponível para o mundo fora deste contêiner

# Run app.py when the container launches
CMD ["python", "app.py"]
# Execute app.py quando o contêiner for iniciado