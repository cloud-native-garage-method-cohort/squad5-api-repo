FROM python:3.7

COPY . .
WORKDIR /app

RUN pip install -r ./requirements.txt
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

EXPOSE 80

ENTRYPOINT ["python"]
CMD ["app.py"]
