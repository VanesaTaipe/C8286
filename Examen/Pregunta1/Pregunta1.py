import asyncio
import time
import random
from concurrent.futures import ThreadPoolExecutor
import copy
def process_booking_requests(requests):

    with ThreadPoolExecutor(max_workers=5) as executor:results = list(executor.map(handle_request,requests))
    return results
def handle_request(request):

 time.sleep(random.uniform(0.1, 0.5)) # Simular tiempo de procesamiento
 return f"Processed request {request['id']} with status: {request['status']}"
async def manage_reservations(requests):
#"""Gestiona reservas asincrónicamente."""
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, process_booking_requests, requests)
    result = await future
    print(result)
async def simulate_requests():
 
    requests = [{'id': i, 'status': 'new'} for i in range(10)]
    await manage_reservations(requests)
    # Simular 10 solicitudes
if __name__ == "__main__":
 asyncio.run(simulate_requests())
