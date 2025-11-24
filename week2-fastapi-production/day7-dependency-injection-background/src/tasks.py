import time

def send_welcome_email(email: str, name: str):
    time.sleep(4)  # simulate real email delay
    print(f"\n[EMAIL SENT] Welcome {name}! Confirmation sent to {email}\n")

def process_uploaded_file(filename: str, size_mb: float):
    time.sleep(3)
    print(f"\n[FILE PROCESSED] {filename} ({size_mb:.1f} MB) saved & converted\n")