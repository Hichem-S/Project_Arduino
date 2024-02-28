FROM python:3.9-slim

ADD Socket.py .
RUN pip install scikit-learn
CMD ["python","./Socket.py"]