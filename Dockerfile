FROM python:3.8.3-alpine3.12

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add fortune

COPY ./clusterFriend/* ./

EXPOSE 8080
CMD [ "gunicorn", "-b", ":8080", "app:app"]