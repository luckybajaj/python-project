from scapy.all import sniff
from PIL import ImageGrab
import time
import os

# Function to capture network packets
def packet_callback(packet):
    print(packet.show())

# Function to capture screen
def capture_screen(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot = ImageGrab.grab()
    screenshot.save(os.path.join(output_dir, f"screenshot_{timestamp}.png"))

def main():
    # Directory to save screenshots
    output_dir = "screenshots"

    # Start packet capture in a separate thread
    print("Starting packet capture...")
    sniff(prn=packet_callback, store=0, count=10)

    # Capture screen at regular intervals
    try:
        while True:
            capture_screen(output_dir)
            print("Screen captured.")
            time.sleep(10)  # Capture screen every 10 seconds
    except KeyboardInterrupt:
        print("Script terminated by user.")

if __name__ == "__main__":
    main()
