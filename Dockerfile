# Usa a imagem oficial do Python 3.10
FROM python:3.10

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala dependências do Django
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do Django
EXPOSE 8000

# Comando para rodar o Django quando o container iniciar
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
