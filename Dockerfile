FROM python:3.12

# Install ffmpeg
RUN apt update && apt install -y ffmpeg

# Set the working directory
WORKDIR /app

# Copy requirements first (to leverage Docker caching)
COPY requirements.txt /app/

# Install dependencies globally in the container
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files
COPY . /app

# Command to run the script
# CMD ["python", "summarizer.py"]

# Expose Streamlit's default port
EXPOSE 8501

# Command to run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]