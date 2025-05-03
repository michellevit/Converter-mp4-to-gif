# converter.py
import os
import subprocess

INPUT_EXT = ".mp4"
OUTPUT_EXT = ".mp3"

# Find the first .mp4 file in the folder
for filename in os.listdir("."):
    if filename.lower().endswith(INPUT_EXT):
        input_file = filename
        output_file = os.path.splitext(filename)[0] + OUTPUT_EXT

        print(f"Converting {input_file} to {output_file}...")

        # Call ffmpeg to convert
        result = subprocess.run([
            "ffmpeg", "-i", input_file,
            "-vn", "-ab", "192k", "-ar", "44100", "-y",
            output_file
        ])

        if result.returncode == 0:
            print("Conversion successful!")
        else:
            print("Conversion failed.")
        break
else:
    print("No MP4 file found in the directory.")
