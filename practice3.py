
def verify_integrity(packet):
    reversed_packet = packet[::-1]

    if packet == reversed_packet:
        print("Integrity Verified: Data packet is valid.")
    else:
        print("Integrity Check Failed: Data packet corrupted.")


data = input("Enter data packet: ")

verify_integrity(data)