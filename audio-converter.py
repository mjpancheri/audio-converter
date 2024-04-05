import sys
import os
import glob

from pydub import AudioSegment


def convert_audio_file(in_file, out_path, audio_format):
    """
    Converts audio files
    """
    try:
      out_file = out_path + os.path.sep + os.path.splitext(os.path.basename(in_file))[0] + '.' + audio_format
      AudioSegment.from_file(file).export(out_file, format=audio_format)
    except FileNotFoundError:
        print("{} does not appear to be valid. Please check.")
    except Exception as e:
        print(e)


input_dir = ""
output_dir = ""
audio_format = "mp3"

if len(sys.argv) < 3:
  print("USAGE:\n./audio-converter.py INPUT_FOLDER OUTPUT_FOLDER [AUDIO_FORMAT (default mp3)]")
else:
  input_dir = sys.argv[1]
  output_dir = sys.argv[2]

  if len(sys.argv) > 3:
    audio_format = sys.argv[3]

  extension_list = ('*.mpeg', '*.wav', '*.mp4')

  os.chdir(input_dir)
  for extension in extension_list:
    for file in glob.glob(extension):
      convert_audio_file(file, output_dir, audio_format)
