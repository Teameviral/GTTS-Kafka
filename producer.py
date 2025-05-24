# producer.py
from gtts import gTTS
from kafka import KafkaProducer
import io

producer = KafkaProducer(bootstrap_servers='localhost:9092')

text = "Hello from Kafka audio streaming using gTTS."
tts = gTTS(text=text, lang='en')

audio_buffer = io.BytesIO()
tts.write_to_fp(audio_buffer)
audio_buffer.seek(0)

# Send the raw bytes to Kafka topic
producer.send('audio-topic', audio_buffer.read())
producer.flush()
print("✅ Audio sent to Kafka topic 'audio-topic'")
