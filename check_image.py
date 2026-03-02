try:
    with open('assets/cyber_eye.jpg', 'rb') as f:
        header = f.read(10)
        print(f"Header: {header}")
        if header.startswith(b'\xff\xd8'):
            print("Valid JPEG header detected.")
        elif header.startswith(b'\x89PNG\r\n\x1a\n'):
             print("Valid PNG header detected.")
        elif b'html' in header.lower() or b'<!doctype' in header.lower():
             print("ERROR: File is HTML (likely an error page saved as image).")
        else:
             print("Unknown file header.")
except Exception as e:
    print(f"Error reading file: {e}")
