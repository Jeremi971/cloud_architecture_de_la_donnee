FROM python:3.12.1
ENV APP_HOME /app
WORKDIR $APP_HOME
# RUN apt-get update
COPY requirements .
RUN pip install -r requirements
COPY . .
CMD ["python3", "app.py"]