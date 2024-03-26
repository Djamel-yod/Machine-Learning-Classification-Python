# Base image with Python 3.8
FROM python:3.12.1

# Install required libraries
WORKDIR /app

RUN pip3 install -r requirements.txt

# Copy your application code
COPY . .

# Expose Streamlit port (default 8501)
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]  
