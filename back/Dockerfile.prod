# pull official base image
FROM python:3.6

# set work directory
RUN mkdir -p /code
WORKDIR /code
COPY . /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get -y install build-essential libssl-dev libffi-dev libblas3 libc6 liblapack3 gcc python3-dev python3-pip cython3
RUN apt-get -y install python3-numpy python3-scipy
RUN apt install -y netcat


# install dependencies
RUN pip install virtualenvwrapper
RUN python3 -m venv /venv
RUN /venv/bin/pip install -U pip
RUN /venv/bin/pip install --upgrade setuptools
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt
RUN if [ -f manage.py ]; then /venv/bin/python manage.py collectstatic --noinput; fi

RUN chmod 755 /code/entrypoint.sh
# run entrypoint.sh

ENTRYPOINT ["sh","/code/entrypoint.sh"]
