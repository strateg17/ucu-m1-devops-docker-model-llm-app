FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy of requiremtns and install 
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY ..

# Set default command
ENTRYPOINT ["streamlit", "run", "main.py"]
CMD ["--server.port=8050", "--server.address=0.0.0.0"]
