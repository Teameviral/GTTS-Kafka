# 🎧 Audio Streaming Architecture with Kafka & gTTS

## 1. Producer (Audio Generator + Kafka Producer)
- Uses `gtts` to convert input text to audio (MP3 or WAV bytes).
- Sends the raw audio bytes as messages to Kafka topic: `audio-topic`.
- Uses Kafka Producer client to push data into Kafka broker.

## 2. Kafka Broker
- Acts as a messaging system.
- Manages topics and stores messages temporarily.
- Your `audio-topic` holds the audio byte stream messages.
- Kafka ensures reliable, scalable, and ordered delivery of messages.

## 3. Consumer (Kafka Consumer + Audio Player)
- Subscribes to `audio-topic`.
- Receives audio byte messages from Kafka.
- Decodes and plays audio or saves it to a file.
- Optionally, can process or analyze audio further.

---

## How Kafka fits in here:
Kafka is a message queue / publish-subscribe system acting as a reliable middle layer.

**Flow:**  
Producers send audio chunks → Kafka stores and manages them → Consumers receive and process.

---

# 🔍 How to explore Kafka state and messages

### Step 1: List Topics  
Inside Kafka container or via command line tools:

```bash
kafka-topics --bootstrap-server localhost:9092 --list
```

Next steps to test your audio streaming setup:
1. Run your Producer script

Make sure your producer script is configured to send audio data to the audio-topic Kafka topic. You mentioned using `gtts` to convert text to speech and then sending audio bytes.

1. Run your producer:

```bash
python producer.py
```

```bash
✅ Audio sent to Kafka topic 'audio-topic'
```

2. Run your Consumer script
Your consumer should be listening to audio-topic, reading the audio bytes, and playing or saving them.

Run your consumer:

```bash
python consumer.py
```

You should see the consumer printing logs about receiving audio messages, possibly saving files or playing audio.

In Consumer, you can see: 

🔄 Waiting for audio messages...
🔊 Playing received audio...
🔊 Playing received audio...
