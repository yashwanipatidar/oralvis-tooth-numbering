FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install Ultralytics YOLOv8 (in case not in requirements)
RUN pip install ultralytics

# Copy all project files
COPY . .

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Default command (change as needed)
CMD ["python", "train_yolov8.py"]
