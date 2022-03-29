import subprocess
import argparse

def main(cmdline_args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, default="google.com", help="The url to ping")
    args = parser.parse_args(cmdline_args)

    cmd_tokens = [
        "ping",
        "-t",
        args.url,
    ]
    try:
        proc = subprocess.Popen(
            cmd_tokens,
        )
        proc.communicate()

    except KeyboardInterrupt:
        return
