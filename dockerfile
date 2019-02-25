FROM python:3

RUN pip3 install tensorflow
RUN mkdir /models
COPY makemodel.py /models/makemodel.py
RUN python3 /models/makemodel.py
RUN rm /models/makemodel.py
