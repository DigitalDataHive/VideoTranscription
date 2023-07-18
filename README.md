# VideoTranscription

To assist with your investigations on video evidence files, here is a program that transcribes an inputted video file to text: Transcript_Video.py 

The program will prompt you to enter the path to the video file you want to transcribe and the path where you want to save the transcription. The transcription will be saved in the specified text file.

Make sure to install the necessary dependencies by running the following commands before executing the code:
pip install moviepy 
pip install SpeechRecognition
brew install ffmpeg (for Macs or Linux based systems)

The program relies on the Google Web Speech API for speech recognition, so an active internet connection is necessary.

The following is a description of how Transcribe_Video.py functions: 

The scripts imports the following libraries: 
‘os’ for file operations
‘moviepy.editor’ from the moviepy library for video processing
‘speech_recognition’ as ‘sr’ for speech recognition capabilities.

The ‘transcribe_video’ function takes two parameters: ‘video_path’ (the path to the video file) and ‘output_path’ (the path to save the transcription). It performs the following steps:
It loads the video file using ‘moviepy.editor.VideoFileClip()’ and extracts the audio 
The audio is saved as a temporary WAV file using the ‘write_audiofile()’ method. (Specified ‘codec="pcm_s16le"’ to ensure compatibility with the SpeechRecognition library). 
The SpeechRecognition library is used to perform the speech recognition. The ‘sr.Recognizer()’ object is created, and the audio file is opened using ‘sr.AudioFile()’. The audio is then recorded using the ‘record()’ method.
The recorded audio is passed to the ‘recognize_google()’ method to perform speech recognition. The resulting transcription is stored in the ‘transcription’ variable.
 The temporary audio file is deleted using ‘os.remove()’ to clean up.
 The transcription is saved to the specified output file using `open()` in write mode. The content is written using the ‘write()’ method of the file object.
 Finally, a message is printed to indicate the location where the transcription is saved.

In the main section of the code, the program prompts the user to enter the path to the video file they want to transcribe. It checks if the file exists using ‘os.path.isfile()’ and displays an error message if the path is invalid. 

The program then prompts the user to enter the path where they want to save the transcription (including the file name and extension). If the file path is valid, the `transcribe_video` function is called with the provided video file path and output file path.

