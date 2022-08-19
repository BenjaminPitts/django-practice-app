import socket

conn = socket.create_connection(("carbon.hostedgraphite.com", 2003))
conn.send("8770573a-2e24-4ad5-9d1f-f69afca83321.test.python.tcp_socket 1.2\n")
conn.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("8770573a-2e24-4ad5-9d1f-f69afca83321.test.python.udp_socket 2.2\n", ("carbon.hostedgraphite.com", 2003))

print 'metrics sent'
