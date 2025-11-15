import os
import subprocess

INPUT_EXT = ".mp4"
OUTPUT_EXT = ".gif"

# Basic settings for GIF output
FPS = 12
WIDTH = 800

for filename in os.listdir("."):
    if filename.lower().endswith(INPUT_EXT):
        input_file = filename
        output_file = os.path.splitext(filename)[0] + OUTPUT_EXT

        print(f"Converting {input_file} to {output_file}...")

        # Build the FFmpeg command
        cmd = [
            "ffmpeg",
            "-y",
            "-i", input_file,
            "-vf", f"fps={FPS},scale={WIDTH}:-1:flags=lanczos",
            "-loop", "0",
            output_file,
        ]

        # Run FFmpeg but capture ALL output
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            print("Conversion successful!")
        else:
            print("Conversion unsuccessful.")
            print("\nError log:")
            print(result.stderr)

        break
else:
    print("No MP4 file found in the directory.")
