import logging
import asyncio

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def read_file(filepath):
    loop = asyncio.get_event_loop()
    with open(filepath, 'r') as f:
        data = await loop.run_in_executor(None, f.read)
    return data
