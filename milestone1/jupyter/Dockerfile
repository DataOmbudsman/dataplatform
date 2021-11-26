FROM python:3.7-slim

RUN mkdir src

WORKDIR /src

RUN pip install jupyter

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8889", "--no-browser", "--allow-root"]

# build image:                          docker build -t af/lp-jupyter .
# create container from image:          docker run -p 8889:8889 af/lp-jupyter
