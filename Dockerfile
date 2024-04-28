### Example Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9.17-bookworm

ARG ARTIFACTORY_URL=https://artifactory.euw.platformservices.io/artifactory


# Copy the current directory contents into the container at /etl_application
COPY etl_application /etl_application
COPY etl_application/etl_application/environment.yaml /usr/local/lib/python3.9/site-packages/etl_application/environment.yaml
# Set the working directory to /etl_application
WORKDIR /etl_application

# Install any needed packages specified in requirements.txt
RUN apt update && \
      apt install -y curl 
RUN apt install -y vim

RUN pip install --upgrade pip && \
    pip install .

ENV API_CALLS=1000
ENV API_RATE_LIMIT=1

# Run app.py when the container launches
#CMD tail -f /dev/null
CMD ["run_etl"]
#ENTRYPOINT ["./run.sh"]
