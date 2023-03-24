set ip_addr=192.169.160.225
set subnet_mask=255.255.255.224
set default_gateway=192.168.160.1

netsh interface ipv4 set address "Ethernet" static %ip_addr% %subnet_mask% %default_gateway%