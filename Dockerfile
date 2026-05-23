FROM python:alpine

WORKDIR /e-commerce-api

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "alembic upgrade head && uvicorn main:app --reload"]