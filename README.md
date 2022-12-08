# audioToText
Install using <pre>python -m pip install git+https://github.com/matt-manes/audioToText</pre><br>
Git must be installed and in your PATH.<br>
audioToText is a module for extracting text from mp3 and wav audio recordings that are hosted locally or on the web.<br>
Note: you still need to be connected to the internet event if you're only processing local files.<br>
Usage:<br>
<pre>
from audioToText import getTextFromUrl, getTextFromWav, getTextFromMp3
#For web hosted audio (mp3 or wav needs to be specified in the second argument)
text = getTextFromUrl('https://somewebsite.com/the-page-where-we-keep-sounds/guess-what-im-saying.mp3', '.mp3')
#For local files
text = getTextFromMp3('some/filePath/someAudio.mp3')
#or
text = getTextFromWav('some/other/filePath/someOtherAudio.wav')
</pre>
