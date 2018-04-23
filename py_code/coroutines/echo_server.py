import socket

async def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SQL_SOCKET, SO_REUSEADDR, True)

    sock.bind(address)

    sock.listen(5)

    while True:
        client, addr = await sock.accept()

        await spawn(echo_client(client, addr))

async def echo_client(client, addr):
    print("Connection from ", addr)

    async with client:
        while True:
            data = await client.recv(1000000)
            if not data:
                break

            await client.sendall(data)

    print("Connection closed")

