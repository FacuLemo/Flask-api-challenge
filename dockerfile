FROM python:3.11.5-alpine3.18
COPY . /Api-paises
WORKDIR /Api-paises

RUN pip install -r requirements.txt

EXPOSE 5040

#ENTRYPOINT [ "python3" ]
CMD ["sh", "run.sh"]