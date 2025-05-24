# consumer.py
from kafka import KafkaConsumer
from pydub import AudioSegment
from pydub.playback import play
import io

consumer = KafkaConsumer(
    'audio-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='audio-group'
)

print("🔄 Waiting for audio messages...")

for message in consumer:
    audio_data = message.value
    audio = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")
    print("🔊 Playing received audio...")
    play(audio)
