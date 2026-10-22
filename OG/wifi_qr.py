#pip install qrcode[pil]
import platform
import subprocess
import re
import qrcode


def get_wifi_info():
    system = platform.system()

    if system == "Windows":
        # Get the currently connected SSID
        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        ssid_match = re.search(r"^\s*SSID\s*:\s*(.+)$", result.stdout, re.MULTILINE)

        if not ssid_match:
            raise RuntimeError("Could not determine the current Wi-Fi network.")

        ssid = ssid_match.group(1).strip()

        # Get the saved password for that SSID
        profile = subprocess.run(
            ["netsh", "wlan", "show", "profile", f"name={ssid}", "key=clear"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        password_match = re.search(
            r"^\s*Key Content\s*:\s*(.*)$",
            profile.stdout,
            re.MULTILINE
        )

        if not password_match:
            raise RuntimeError(
                "The Wi-Fi password could not be retrieved. "
                "The network may not have a saved password."
            )

        password = password_match.group(1).strip()
        return ssid, password

    elif system == "Linux":
        # NetworkManager's nmcli can report the active connection.
        result = subprocess.run(
            ["nmcli", "-t", "-f", "ACTIVE,SSID", "dev", "wifi"],
            capture_output=True,
            text=True
        )

        ssid = None

        for line in result.stdout.splitlines():
            if line.startswith("yes:"):
                ssid = line[4:]
                break

        if not ssid:
            raise RuntimeError("Could not determine the current Wi-Fi network.")

        # Ask NetworkManager for the saved Wi-Fi password.
        result = subprocess.run(
            ["nmcli", "-s", "-g", "802-11-wireless-security.psk",
             "connection", "show", ssid],
            capture_output=True,
            text=True
        )

        password = result.stdout.strip()

        if not password:
            raise RuntimeError(
                "Could not retrieve the Wi-Fi password. "
                "You may need appropriate permissions."
            )

        return ssid, password

    elif system == "Darwin":
        # macOS: airport identifies the connected SSID.
        result = subprocess.run(
            ["/System/Library/PrivateFrameworks/Apple80211.framework/"
             "Versions/Current/Resources/airport", "-I"],
            capture_output=True,
            text=True
        )

        ssid_match = re.search(r"\s*SSID:\s*(.+)", result.stdout)

        if not ssid_match:
            raise RuntimeError("Could not determine the current Wi-Fi network.")

        ssid = ssid_match.group(1).strip()

        # security finds the saved password in the macOS Keychain.
        result = subprocess.run(
            ["security", "find-generic-password", "-wa", ssid],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(
                "Could not retrieve the Wi-Fi password. "
                "macOS may require Keychain authorization."
            )

        password = result.stdout.strip()
        return ssid, password

    else:
        raise RuntimeError(f"Unsupported operating system: {system}")


def escape_wifi(value):
    """Escape characters required by the Wi-Fi QR-code format."""
    return (
        value.replace("\\", "\\\\")
             .replace(";", "\\;")
             .replace(",", "\\,")
             .replace(":", "\\:")
             .replace('"', '\\"')
    )


def create_qr(ssid, password, filename="wifi_qr.png"):
    # WPA/WPA2/WPA3 networks generally use this format.
    wifi_data = (
        f'WIFI:T:WPA;'
        f'S:{escape_wifi(ssid)};'
        f'P:{escape_wifi(password)};;'
    )

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(wifi_data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(filename)

    return filename


def main():
    try:
        ssid, password = get_wifi_info()

        filename = create_qr(ssid, password)

        print(f"Connected network : {ssid}")
        print(f"QR code saved to  : {filename}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()