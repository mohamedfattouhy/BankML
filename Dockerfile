FROM ubuntu:22.04

WORKDIR /BankMLApp

# Install Python
RUN apt-get -y update && \
    apt-get install -y python3-pip

# Install project dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install bankml package
COPY pyproject.toml .
COPY ./src/bankml/ ./src/bankml
RUN pip install .

COPY main.py .
COPY ./api/api.py ./api/api.py
COPY ./api/features/features_class.py ./api/features/features_class.py
COPY ./model/ ./model/
COPY ./configuration/ ./configuration/

# add src/ to PYTHONPATH
ENV PYTHONPATH="./src/"

COPY ./run.sh .

CMD ["bash", "-c", "./run.sh"]
