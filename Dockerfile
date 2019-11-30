FROM python:3.6-jessie
RUN apt update
#RUN apt install -y gunicorn
WORKDIR /app
ADD pystan-2.19.1.1-cp36-cp36m-manylinux1_x86_64.whl /app
RUN pip install pystan-2.19.1.1-cp36-cp36m-manylinux1_x86_64.whl
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /app
ADD forecast_model.pckl /app

RUN rm /app/pystan-2.19.1.1-cp36-cp36m-manylinux1_x86_64.whl

ENV PORT 8080
#CMD ["gunicorn", "app:app", "--config=config.py"]
CMD ["python", "/app/app.py"]

