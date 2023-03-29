FROM python:latest
RUN pip install requests
ADD po.csv /tmp/po.csv
WORKDIR /tmp
CMD [ "python", "-u", "test.py" "04", "1", "3"]
