FROM python:3.12.1-slim-bullseye

RUN apt-get update && apt-get install -y

RUN mkdir -p  /home/flaskapp

WORKDIR /home/flaskapp

EXPOSE 8000

COPY . .

RUN chmod +x ./entrypoint.sh

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
