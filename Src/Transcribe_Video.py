import os
import moviepy.editor as mp
import speech_recognition as sr

def transcribe_video(video_path, output_path):
    # Load the video file
    video = mp.VideoFileClip(video_path)

    # Extract the audio from the video
    audio = video.audio

    # Save the audio as a temporary WAV file
    audio_path = "temp.wav"
    audio.write_audiofile(audio_path, codec="pcm_s16le")

    # Use SpeechRecognition library to transcribe the audio
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)

    # Perform speech recognition
    try:
        transcription = r.recognize_google(audio)
    except sr.UnknownValueError:
        transcription = "Transcription failed: Audio could not be transcribed."
    except sr.RequestError:
        transcription = "Transcription failed: Unable to connect to the Google Web Speech API."

    # Delete the temporary audio file
    os.remove(audio_path)

    # Save the transcription to a text file
    with open(output_path, "w") as f:
        f.write(transcription)

    print(f"Transcription saved to: {output_path}")

if __name__ == "__main__":
    # Prompt user for video file path
    video_path = input("Enter the path to the video file: ")

    # Check if the file exists
    if not os.path.isfile(video_path):
        print("Invalid file path. Please provide a valid path to the video file.")
    else:
        # Prompt user for output file path
        output_path = input("Enter the path to save the transcription (including the file name and extension): ")

        # Call the transcribe_video function with the provided video file path and output file path
        transcribe_video(video_path, output_path)
