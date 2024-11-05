FROM python:3
COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip install -r requirements.txt --break-system-packages
COPY . /
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
