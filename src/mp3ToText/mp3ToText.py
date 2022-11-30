from datetime import datetime
import os
from pathlib import Path
from pydub import AudioSegment
import requests
import speech_recognition
from whosYourAgent import getAgent

root = Path(__file__).parent

""" Extract text from an mp3 file located at a given url. """

def downloadMp3File(url:str)->Path:
    """ Downloads an mp3 file to
    a folder named audio in
    the same folder as this file.\n
    Returns a Path object for the
    saved file."""
    dest = root/'audio'
    dest.mkdir(parents=True, exist_ok=True)
    mp3Path = (dest/datetime.now().timestamp()).with_suffix('.mp3')
    source = requests.get(url, headers={'User-Agent': getAgent()})
    with mp3Path.open('wb') as file:
        file.write(source.content)
    return mp3Path

def convertMp3ToWav(mp3Path:Path)->Path:
    """ Converts an mp3 file to a wav file
    of the same name, deletes the mp3 file, 
    and returns a Path object for the wav file."""
    audio = AudioSegment.from_mp3(mp3Path)
    wavPath = mp3Path.with_suffix('.wav')
    audio.export(wavPath, format='wav')
    mp3Path.unlink()
    return wavPath

def extractTextFromWav(wavPath:Path)->str|None:
    """ Extracts and returns text from wav file. """
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(str(wavPath)) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
    wavPath.unlink()
    return text

def getText(url:str)->str:
    """ Returns text from an mp3 file
    located at the given url."""
    return extractTextFromWav(convertMp3ToWav(downloadMp3File(url)))

def cleanUp():
    """ Removes any files from the audio directory
    older than 5 minutes."""
    audioDir = (root/'audio')
    if audioDir.exists():
        for file in (root/'audio').glob('*.*'):
           if (datetime.now().timestamp() - os.stat(file).st_ctime) > (60 * 5):
               file.unlink()