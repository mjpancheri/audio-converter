# video-downloader
Project using the `pydub` lib to convert audio files.

## Config
> You need to import `pydub`
```bash
pip install pytube
```

> To install `pip`, you can use:
```bash
sudo pacman -Sy python-pip
```  

## How it works
> Inform input and output folders, and audio format (optional, default mp3)

### command-line
```bash
python audio-converter.py INPUT_FOLDER OUTPUT_FOLDER [AUDIO_FORMAT]
```

### Tips
> You can generate a installer with `pyinstaller`
```bash
pyinstaller audio-converter.py
```
