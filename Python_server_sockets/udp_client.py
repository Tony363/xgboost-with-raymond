

def client():
    import time
    import socket
    # for pings in range(5):
    i = 0
    while i < 2:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(1.0)
        message = b'test'
        addr = ("127.0.0.1", 12000)

        start = time.time()
        client_socket.sendto(message, addr)
        try:
            data, server = client_socket.recvfrom(1024)
            end = time.time()
            elapsed = end - start
            # print(f'{server} {data} {elapsed}')
            # time.sleep(1)
        except socket.timeout:
            print('REQUEST TIMED OUT')
            time.sleep(1)
            i += 1

        
        # except KeyboardInterrupt:
        #     raise KeyboardInterrupt()
    return client_socket

