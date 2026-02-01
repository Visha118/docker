#------------ Stage1: build stage
FROM python:3.12-alpine AS builder

WORKDIR /app

RUN apk add --no-cache gcc musl-dev

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt
#------- Stage2: runtime
FROM python:3.12-alpine

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /install /usr/local

# Copy app source code
COPY . .

EXPOSE 7777

ENTRYPOINT ["python", "app.py"]
