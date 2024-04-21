#!/usr/bin/env python

import glob
import os
import subprocess

from dotenv import load_dotenv
from openai import OpenAI

local_dotenv = os.path.join(os.path.dirname(__file__), ".env")
api_key_from_env = os.getenv("OPENAI_API_KEY")

src_dir = "./src"  # replace with your source directory
dst_dir = "./mp3"  # replace with your destination directory

# Get list of all .WAV files in the source directory
wav_files = glob.glob(os.path.join(src_dir, "*.WAV"))
# Loop over each .WAV file
for wav_file in wav_files:
    # Get the base name of the file (without extension)
    base_name = os.path.basename(wav_file).split(".")[0]

    # Construct the destination file path
    mp3_file = os.path.join(dst_dir, base_name + ".mp3")

    # Check if the mp3 file already exists
    if os.path.exists(mp3_file):
        # If it does, skip the conversion
        continue
    # Run ffmpeg to convert the .WAV file to .mp3
    subprocess.run(["ffmpeg", "-i", wav_file, mp3_file])

# Get list of all .mp3 files in the destination directory
mp3_files = glob.glob(os.path.join(dst_dir, "*.mp3"))

# Loop over each .mp3 file
for mp3_file in mp3_files:
    # Get the size of the file in bytes
    file_size = os.path.getsize(mp3_file)
    # Convert the size to megabytes
    file_size_mb = file_size / (1024 * 1024)
    # If the file size is greater than 25MB
    if file_size_mb > 25:
        print(f"The file {mp3_file} exceeds 25MB.")
        exit(1)

client = OpenAI(api_key=api_key_from_env)
# Define the destination directory for the text files
txt_dir = "./txt"
# Ensure the txt directory exists
os.makedirs(txt_dir, exist_ok=True)
for mp3_file in mp3_files:
    # Get the base name of the file (without extension)
    base_name = os.path.basename(mp3_file).split(".")[0]
    # Construct the destination file path
    txt_file = os.path.join(txt_dir, base_name + ".txt")
    # Check if the txt file already exists
    if os.path.exists(txt_file):
        # If it does, skip the transcription
        print(f"The file {txt_file} already exists, skipping transcription.")
        continue
    print(f"Transcribing the file {mp3_file}...")
    # Open the audio file
    with open(mp3_file, "rb") as audio_file:
        # Create a transcription of the audio file
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            language="ko",
            file=audio_file,
        )
        # Get the text from the transcript
        text = transcript.text
        # Write the text to a .txt file
        with open(txt_file, "w") as output_file:
            output_file.write(text)
