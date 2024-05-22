FROM python:3.9

WORKDIR /sl_map_test

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8501