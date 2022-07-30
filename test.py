import socket

addr = ('', 8090)
if socket.has_dualstack_ipv6():
    s = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
    print('supports dual stack TCP')
else:
    s = socket.create_server(addr)
    print('Doesn"t support dual stack')
