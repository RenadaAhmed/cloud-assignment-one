#base image
FROM python
COPY . /Cloud_assig1
WORKDIR /Cloud_assig1
Run pip install numpy
CMD python pyCode.py
