import os
import argparse

def main(cmdline_args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="google.com", help="The url to ping")
    args = parser.parse_args(cmdline_args)

    cmd = f"ping -t {args.url}"
    try:
        os.system(cmd)
    except KeyboardInterrupt:
        return
