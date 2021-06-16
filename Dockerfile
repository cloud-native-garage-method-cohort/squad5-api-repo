FROM python:3.7

WORKDIR /app
COPY . .

RUN pip install -r ./requirements.txt
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

EXPOSE 8088

ENTRYPOINT ["python"]
CMD ["app.py"]
