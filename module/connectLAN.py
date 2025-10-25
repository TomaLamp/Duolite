import socket
import scapy.all as sc
import psutil
import pygame
from pygame import *
import select

def get_ip():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))  
        local_ip = s.getsockname()[0]
    finally:
        s.close()

    netmask="0"
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.address == local_ip:
                netmask = getattr(addr, "netmask", None)

    ip = netmask.split('.')
    nb = 0
    for i in range(4):
        bit = str(bin(int(ip[i])))[2:]
        for j in range(len(bit)):
            if bit[j]=='0':
                break
            else:
                nb+=1
    
    return local_ip+"/"+str(nb)

def netScan(ip):
    frame = sc.Ether(dst="ff:ff:ff:ff:ff:ff") / sc.ARP(pdst=ip)

    answered_list = sc.srp(frame, timeout = 3, verbose = False)[0]
    result = []
    for i in range(0,len(answered_list)):
        result.append(answered_list[i][1].psrc)

    return result


def createRoom(code):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 5555))
        s.listen()
        s.setblocking(False)
        
        data = b""
        connexion = False
        while True:
            try:
                conn, addr = s.accept()
                connexion = True
                conn.setblocking(True)
            except BlockingIOError:
                pass

            if connexion:
                data = conn.recv(1024)
                
                if str(data, "utf-8", errors='ignore')==code:
                    conn.send(b"OK")
                    return conn
                elif str(data, "utf-8", errors='ignore')!="" :
                    conn.send(b"KO")
                    conn.close()
                    connexion=False

            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]

                        if x>750 and x<780 and y>115 and y<145:
                            return None

                if (event.type == pygame.QUIT): 
                        exit()


def joinRoom(code):
    ips = netScan(get_ip())

    for ip in ips:
        frame = sc.IP(dst=ip) / sc.TCP(dport=5555, flags="S")
        answer = sc.sr(frame, timeout=1, verbose=0)[0]
        for ans in answer:
            if ans[1][sc.TCP].flags == "SA":
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, 5555))
                s.send(bytes(code, "utf-8"))

                s.settimeout(3.0)
                try:
                    data = s.recv(1024)
                except socket.timeout:
                    data = b"KO"

                if str(data, "utf-8", errors='ignore')=="OK":
                    return s
                elif str(data, "utf-8", errors='ignore')=="KO":
                    s.close()


def isConnClose(conn):
    isclose = False
    readable, _, _ = select.select([conn], [], [], 1)
    if conn in readable:
        try:
            data = conn.recv(1024)
            if not data:
                isclose = True
        except ConnectionAbortedError:
            isclose=True
    
    return isclose

