FROM python:3.12-slim AS build

# Set the working directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    python3-dev \
    pkg-config \
    libffi-dev \
    && pip install --upgrade pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Verify that Django is installed in the build stage
RUN python -m django --version

# Copy the application code
COPY . .

# Stage 2: Production Stage with Gunicorn and Nginx
FROM python:3.12-slim AS runtime

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Set the working directory
WORKDIR /app

# Install necessary runtime dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only the necessary files from the build stage
COPY --from=build /app /app

# Copy the installed dependencies from the build stage
COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

# Verify that Django is installed in the build stage
RUN python -m django --version

# Install Gunicorn
RUN pip install gunicorn

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80
EXPOSE 8000

# Start Gunicorn and Nginx
CMD service nginx start && gunicorn --bind 0.0.0.0:8000 ExpenseTracker.wsgi:application
