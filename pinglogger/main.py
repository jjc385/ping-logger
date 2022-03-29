import subprocess
import argparse

from .prependtimestamp import prepend_timestamp

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
            stdout=subprocess.PIPE,
        )

        for line in proc.stdout:
            line = line.decode()
            line = line.strip()
            line = prepend_timestamp(line)
            print(line)

        proc.communicate()

    except KeyboardInterrupt:
        return
