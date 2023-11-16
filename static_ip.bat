set ip_addr=192.169.160.225
set subnet_mask=255.255.255.224
set default_gateway=192.168.160.1
set dns_server=192.168.155.252

netsh interface ipv4 set address "Ethernet" static %ip_addr% %subnet_mask% %default_gateway%

netsh interface ipv4 set dnsservers "Ethernet" static %dns_server% primary