FROM python:3

WORKDIR /usr/src
COPY . /usr/src
RUN git clone https://github.com/joaoventura/flask-static-site
RUN pip install --no-cache-dir -r flask-static-site/requirements.txt

EXPOSE 8000

CMD ["python3","./flask-static-site/site.py"]