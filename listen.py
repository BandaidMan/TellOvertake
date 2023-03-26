from scapy.all import *

# Enter the interface to sniff on
sniff_iface = "eth0"

# Create a packet capture filter
pkt_filter = "tcp"

# Create a file to save the capture
save_file = "capture.pcap"

# Start the sniffer
sniff(iface=sniff_iface, filter=pkt_filter, prn=lambda x:x.show(), store=1, offline=save_file)