# MP4 to GIF Converter

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)](https://www.python.org/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-7.1.1-green?logo=ffmpeg)](https://ffmpeg.org/)

This simple project converts a single `.mp4` file into an `.gif` using [FFmpeg](https://ffmpeg.org/).

## How to Use

1. Place your `.mp4` file in the root of this project folder  
   ⚠️ Make sure it's the **only `.mp4` file** in the folder.
2. Double-click:
   - On Windows: `run-converter.bat`
   - On macOS/Linux (if supported): `./run-converter.bat`
3. The script will extract the audio and save it as a `.gif`.

The converted file will appear in the same folder with the same name.

## Requirements

- [FFmpeg](https://ffmpeg.org/download.html) must be installed and added to your system `PATH`.
- [Python](https://www.python.org/) 3.6+

To check if FFmpeg is installed, run:

```bash
ffmpeg -version
```
