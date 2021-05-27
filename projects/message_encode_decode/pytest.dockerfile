FROM python:3.8.2-alpine
ADD . /message_encode_decode
WORKDIR /message_encode_decode
RUN pip install -r requirements-test.txt
CMD pytest tests/test_encode_decode.py
