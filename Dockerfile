FROM python:3.7

COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["flask"]
CMD ["run", "--host", "0.0.0.0"]