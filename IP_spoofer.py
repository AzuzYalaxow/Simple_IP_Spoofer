import sys 
from scapy.all import sr,IP,ICMP 
from faker import Faker 


fake=Faker()

def generate_fake_ip():
    return fake.ipv4()


def craft_and_send_packet(source_ip, destination_ip):
    packet=IP(src=source_ip, dst=destination_ip) / ICMP()

    answers, _=sr(packet,verbose=0,timeout=5)
    return answers 

def display_packet_summary(sent, recieved):
    print(f"[+] Sent Packet: {sent.summary()}")
    print(f"[+] recieved : {recieved.summary()}")


if len(sys.argv)!=2:
    print(f"[-] Error! Please run as: {sys.argv[0]} <dst_ip>")
    sys.exit(1)

destination_ip=sys.argv[1]
source_ip=generate_fake_ip()

answers=craft_and_send_packet(source_ip,destination_ip)

for sent,received in answers:
    display_packet_summary(sent,received)
    