# Stage 1: Builder
FROM python:3.11-alpine AS builder

WORKDIR /app

COPY requirements.txt .

# Install dependencies globally (no --user)
RUN pip install  -r requirements.txt


# Stage 2: Runtime
FROM python:3.11-alpine

WORKDIR /app

# Copy installed packages from builder image
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11

COPY --from=builder /usr/local/bin /usr/local/bin

# Copy your actual app code
COPY ./app .

# Add user and assign ownership
RUN adduser -D appuser && chown -R appuser /app

USER appuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6000"]
