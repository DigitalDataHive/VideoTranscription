# VideoTranscription

## Description

To assist with your investigations on video evidence files, this program transcribes an inputted video file to text using the Google Web Speech API for speech recognition. Please ensure you have an active internet connection since the program relies on the API for transcription.

## Usage

1. Install the necessary dependencies by running the following commands before executing the code:

   ```bash
   pip install moviepy
   pip install SpeechRecognition
   brew install ffmpeg # For Macs or Linux based systems
   ```

2. Run the program using:
   ```bash 
   python3 Transcript_Video.py
   ```

3. The program will prompt you to enter the path to the video file you want to transcribe and the path where you want to save the transcription. The transcription will be saved in the specified text file.

4. Make sure the video file you want to transcribe does not exceed 10 MB, as this is the limit for single requests sent to the [Google Cloud Speech](https://cloud.google.com/speech-to-text/quotas) using local files.

## Functionality

The program functions as follows:

1. Import the required libraries:
   - `os` for file operations.
   - `moviepy.editor` from the moviepy library for video processing.
   - `speech_recognition` as `sr` for speech recognition capabilities.

2. Define the `transcribe_video` function with two parameters:

   - `video_path` - the path to the video file.
   - `output_path` - the path to save the transcription.

3. The `transcribe_video` function performs the following steps:

   - Load the video file using `moviepy.editor.VideoFileClip()` and extract the audio.
   - Save the audio as a temporary WAV file using the `write_audiofile()` method with the `codec="pcm_s16le"` parameter to ensure compatibility with the SpeechRecognition library.
   - Use the SpeechRecognition library to perform speech recognition. Create a `sr.Recognizer()` object, open the audio file using `sr.AudioFile()`, and record the audio using the `record()` method.
   - Pass the recorded audio to the `recognize_google()` method for speech recognition. The resulting transcription is stored in the `transcription` variable.
   - Delete the temporary audio file using `os.remove()` to clean up.
   - Save the transcription to the specified output file using `open()` in write mode. The content is written using the `write()` method of the file object.
   - Print a message indicating the location where the transcription is saved.

4. In the main section of the code:

   - Prompt the user to enter the path to the video file they want to transcribe.
   - Check if the file exists using `os.path.isfile()` and display an error message if the path is invalid.
   - Prompt the user to enter the path where they want to save the transcription (including the file name and extension).
   - If the file path is valid, call the `transcribe_video` function with the provided video file path and output file path.

## Disclaimer

This program utilizes the [Google Web Speech API](https://cloud.google.com/speech-to-text) for speech recognition. Please ensure you comply with any terms of service and usage limitations set forth by Google Cloud for their API. The developer of this program is not responsible for any misuse or violations of those terms.