from aiokafka import AIOKafkaProducer
import random
import asyncio

async def send_message(producer, broker, message):
    # Send message to the topic
    await producer.send_and_wait("my_topic", message, partition= random.randint(1, 3))
    print(f"Sent message to {broker}")

async def send_multiple():
    brokers = ['localhost:9092', '172.16.46.205.:9093', '172.16.46.25:9094']
    producer = AIOKafkaProducer(bootstrap_servers=brokers)
    
    # Start producer to initialize cluster layout
    await producer.start()
    try:
        while True:
            tasks = []
            for i, broker in enumerate(brokers):
                message = f"Hello message to broker {i+1}".encode('utf-8')
                # Schedule each send_message task to run concurrently
                task = asyncio.create_task(send_message(producer, broker, message))
                tasks.append(task)
                # Wait 2 seconds between scheduling the next message
                await asyncio.sleep(2)

            # Wait for all messages to be sent
            await asyncio.gather(*tasks)
    finally:
        # Stop producer and wait for all pending messages to be delivered or expire
        await producer.stop()

# Run the async function
asyncio.run(send_multiple())
