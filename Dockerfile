# Use the official Python base image
FROM python:3.9-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy the code into the container
COPY . /app

# Install the required dependencies
RUN pip install pyannote.audio soundfile torch torchvision torchaudio

# Install libsndfile1 for soundfile support
RUN apt-get update && apt-get install -y libsndfile1

# Set the entrypoint command
CMD ["python", "/app/diarization.py"]
