FROM python:3

RUN pip3 install tensorflow
COPY makemodel.py /makemodel.py
RUN python3 /makemodel.py
RUN rm /makemodel.py
