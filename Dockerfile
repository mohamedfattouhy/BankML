FROM ubuntu:22.04

WORKDIR /BankMLApp

# Install Python
RUN apt-get -y update && \
    apt-get install -y python3-pip

# Install project dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY app/api.py ./app/
COPY app/features/ ./app/features/
COPY model/ ./model/
COPY src/ ./src/
COPY configuration/ ./configuration/

COPY run.sh .

CMD ["bash", "-c", "./run.sh"]
