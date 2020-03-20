FROM python:3.7

# app directory
WORKDIR /flaskapp

# copy all the files to the container 
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# specify port number that needs to be exposed
EXPOSE 5000

# command for running the aplication
CMD ["python", "./app.py"]
