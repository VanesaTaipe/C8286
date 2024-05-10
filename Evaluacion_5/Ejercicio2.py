from concurrent.futures import ThreadPoolExecutor
import copy
import random
import time
import asyncio
def add_reservation(reservations, reservation):
    """Agrega una nueva reserva a la lista de reservas de manera inmutable."""
    return reservations + [reservation]

def cancel_reservation(reservations, reservation_id):
    """Cancela una reserva por ID, inmutablemente."""
    return [res for res in reservations if res['id'] != reservation_id]

def update_reservation(reservations, reservation_id, new_details):
    """Actualiza una reserva por ID, inmutablemente."""
    return [res if res['id'] != reservation_id else {**res, **new_details} for res in reservations]
def process_booking_requests(requests):
    """Procesa una lista de solicitudes de reserva concurrentemente."""
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(handle_request, requests))
    return results

def handle_request(request):
    """Maneja una solicitud individual simulando cierta lógica y tiempo de procesamiento."""
    # Simulación de procesamiento: modificar según la lógica de negocio
    time.sleep(random.uniform(0.1, 0.5))  # Simular tiempo de procesamiento
    return f"Processed request {request['id']} with status: {request['status']}"

async def manage_reservations(requests):
    """Gestiona reservas asincrónicamente."""
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, process_booking_requests, requests)
    result = await future
    print(result)

async def simulate_requests():
    """Simula la llegada de solicitudes de reserva."""
    requests = [{'id': i, 'status': 'new'} for i in range(10)]  # Simular 10 solicitudes
    await manage_reservations(requests)

if __name__ == "__main__":
    asyncio.run(simulate_requests())