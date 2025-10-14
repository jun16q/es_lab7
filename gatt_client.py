import struct
import time
from bluepy.btle import Peripheral, UUID, BTLEException, DefaultDelegate

TARGET_DEVICE_ADDR = 'd8:94:7e:7b:0b:6a'

ACCEL_SERVICE_UUID = UUID('00000000-0001-11e1-ffff-ffffffffffbb')
ACCEL_DATA_CHAR_UUID = UUID('00000000-0001-11e1-ffff-ffffffffffcc')
SAMPLING_FREQ_CHAR_UUID = UUID('00000000-0001-11e1-ffff-ffffffffffdd')

CCCD_UUID = UUID('2902')
CCCD_ENABLE_NOTIFY = b'\x01\x00'

SAMPLING_FREQ_TO_WRITE = 20 

class NotificationDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        try:
            x, y, z = struct.unpack('<hhh', data)
            print(f"[Notification] Accel Data: X={x}, Y={y}, Z={z}")
        except struct.error:
            print(f"[Notification] Received raw data (unexpected length {len(data)}): {data.hex()}")

def find_and_connect(target_addr, timeout=10.0):
    try:
        print(f"Connecting to {target_addr}...")
        p = Peripheral(target_addr, 'random')
        print(f"Connected to {target_addr}.")
        return p
    except BTLEException as e:
        print(f"ERROR: Failed to connect to {target_addr}.")
        print(f"Details: {e}")
        return None

def set_sampling_frequency(p, service_uuid, char_uuid, freq_hz):
    try:
        print(f"\n--- Setting Sampling Frequency to {freq_hz} Hz ---")
        svc = p.getServiceByUUID(service_uuid)
        char = svc.getCharacteristics(char_uuid)[0]
        
        freq_byte = freq_hz.to_bytes(1, 'little')
        
        print(f"Found Frequency Characteristic: {str(char)}")
        print(f"Writing value: {freq_byte.hex()}")
        
        char.write(freq_byte, withResponse=True)
        print("Frequency Write SUCCESSFUL.")
        return True
    except Exception as e:
        print(f"ERROR during write operation: {e}")
        return False
        
def enable_notifications(p, service_uuid, char_uuid):
    try:
        print("\n--- Enabling Notifications ---")
        svc = p.getServiceByUUID(service_uuid)
        char_to_notify = svc.getCharacteristics(char_uuid)[0]
        
        cccd = char_to_notify.getDescriptors(forUUID=CCCD_UUID)[0]
        
        print(f"Found Data Characteristic: {str(char_to_notify)}")
        print(f"Found CCCD Descriptor: {str(cccd)}")
        print(f"Writing CCCD value: {CCCD_ENABLE_NOTIFY.hex()}")
        
        cccd.write(CCCD_ENABLE_NOTIFY, withResponse=True)
        print("Notifications Enabled.")
        return True
    except Exception as e:
        print(f"ERROR during notification setup: {e}")
        return False
        
def main():
    peripheral = find_and_connect(TARGET_DEVICE_ADDR)

    if peripheral:
        try:
            peripheral.withDelegate(NotificationDelegate())

            # 1. Writing sampling rate
            if not set_sampling_frequency(peripheral, ACCEL_SERVICE_UUID, SAMPLING_FREQ_CHAR_UUID, SAMPLING_FREQ_TO_WRITE):
                raise Exception("Failed to set sampling frequency.")

            # 2. Enabling notifications
            if not enable_notifications(peripheral, ACCEL_SERVICE_UUID, ACCEL_DATA_CHAR_UUID):
                raise Exception("Failed to enable notifications.")

            print("\n--- Waiting for notifications (Press Ctrl+C to stop) ---")
            while True:
                if peripheral.waitForNotifications(5.0):
                    continue
                print("No new notification in 5 seconds...")
        
        except KeyboardInterrupt:
            print("\nStopping notification loop.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Disconnecting...")
            peripheral.disconnect()
            print("Disconnected.")

if __name__ == "__main__":
    main()
