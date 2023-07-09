FROM python:3.10
EXPOSE 5000
WORKDIR /api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
# docker build -t flask-api .
# docker run -dp 5005:5000 -w /api -v "$(pwd):/api" flask-api