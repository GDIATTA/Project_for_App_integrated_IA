FROM python:3.11
WORKDIR /app
COPY . /app/

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y python3-venv python3-pip

# Créer un venv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Installer les dépendances dans le venv
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -r /requirements.txt

CMD [ "python", "run.py" ]