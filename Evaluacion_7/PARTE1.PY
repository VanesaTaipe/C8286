import asyncio
import pickle
import socket

# Servidor

async def submit_job(reader, writer):
    # ...

async def get_results(reader, writer):
    # ...

async def process_sum(reader, writer):
    data_size = int.from_bytes(await reader.read(4), 'little')
    numbers = pickle.loads(await reader.read(data_size))
    result = sum(numbers)
    writer.write(pickle.dumps(result))
    await writer.drain()
    writer.close()

async def accept_requests(reader, writer):
    op = await reader.read(1)
    if op[0] == 0:
        await submit_job(reader, writer)
    elif op[0] == 1:
        await get_results(reader, writer)
    elif op[0] == 2:
        await process_sum(reader, writer)

async def main():
    server = await asyncio.start_server(accept_requests, '127.0.0.1', 1936)
    async with server:
        await server.serve_forever()

asyncio.run(main())

# Cliente

def sum_numbers(numbers):
    conn = socket.create_connection(('127.0.0.1', 1936))
    conn.send(b'\x02')
    my_data = pickle.dumps(numbers)
    conn.send(len(my_data).to_bytes(4, 'little'))
    conn.send(my_data)
    result_size = int.from_bytes(conn.recv(4), 'little')
    result = pickle.loads(conn.recv(result_size))
    conn.close()
    return result

def do_request(my_funs, data):
    # ...

if __name__ == '__main__':
    do_request(my_funs, 'Python rocks. Python es divertido'.split(' '))
    result = sum_numbers([1, 2, 3, 4, 5])
    print(f'La suma es: {result}')
