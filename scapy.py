import scapy.all as scapy
import socket
import csv
import datetime

def get_mac(ip):
    try:
        responses, _ = scapy.srp(scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip), timeout=2, verbose=False)
        for response in responses:
            return response[1].hwsrc
    except Exception as e:
        return None

def scan_network(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices = []
    for element in answered_list:
        device = {
            'ip': element[1].psrc,
            'mac': element[1].hwsrc,
            'hostname': None
        }

        try:
            device['hostname'] = socket.gethostbyaddr(device['ip'])[0]
        except socket.herror:
            device['hostname'] = 'Unknown'

        devices.append(device)
    return devices

def save_report(devices, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['IP Address', 'MAC Address', 'Hostname']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for device in devices:
            writer.writerow({
                'IP Address': device['ip'],
                'MAC Address': device['mac'],
                'Hostname': device['hostname']
            })

def main():
    ip_range = "192.168.1.1/24"  # Замените на нужный диапазон IP
    devices = scan_network(ip_range)
    report_filename = f"network_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    save_report(devices, report_filename)
    print(f"Отчет сохранен в {report_filename}")

if __name__ == "__main__":
    main()
