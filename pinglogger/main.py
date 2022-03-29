import os

def main():
    url = "google.com"
    cmd = f"ping -t {url}"

    os.system(cmd)
