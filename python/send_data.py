import serial
import time


def create_message(mode, freq):
    if mode == "OFF":
        freq = 0
    else:
        freq = abs(freq)

    message = f"{mode},{freq}\n"

    return message


def prompt_command():
    while True:
        try:
            raw = input("Enter command or 'q' to quit: ").strip()
            if raw.lower() == "q":
                return None
            parts = raw.split(",")
            if len(parts) != 2:
                print("Invalid format.")
                continue
            mode = parts[0].strip().upper()
            if mode not in ("ON", "OFF"):
                print("Mode must be ON or OFF")
                continue
            freq = int(parts[1].strip())
            return create_message(mode, freq)
        except ValueError:
            print("Parse error")


def main():
    port = "/dev/ttyACM0"
    baud_rate = 460800
    ser = None

    try:
        # Open serial port
        ser = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(1)  # Wait for connection to establish

        while True:
            message = prompt_command()
            if message is None:
                print("Exiting")
                message = "OFF,0\n"
                ser.write(message.encode("utf-8"))
                print(f"Sent: {message.strip()}")
                break
            ser.write(message.encode("utf-8"))
            print(f"Sent: {message.strip()}")

    except serial.SerialException as e:
        print(f"Serial port error: {e}")
        print("Check if:")
        print("  - Device is connected")
        print("  - Port /dev/ttyACM0 exists")
        print("  - You have permissions (try: sudo usermod -a -G dialout $USER)")

    except PermissionError:
        print("Permission denied accessing /dev/ttyACM0")
        print("Run: sudo chmod 666 /dev/ttyACM0")
        print("Or add user to dialout group: sudo usermod -a -G dialout $USER")

    except KeyboardInterrupt:
        print("\nExiting.")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
    finally:
        if ser is not None and ser.is_open:
            print("Close serial port.")
            ser.close()


if __name__ == "__main__":
    main()
