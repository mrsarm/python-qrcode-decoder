#!/usr/bin/env python3

import sys

from pyzbar.pyzbar import decode
from PIL import Image

if len(sys.argv) <= 1 or sys.argv[1] in ('-h', '--help'):
    print("qdec.py: decode the payload of a QR Code image.\n", file=sys.stderr)
    print("Usage: qdec.py <IMAGE FILE>", file=sys.stderr)
    exit(1)

try:
    with Image.open(sys.argv[1]) as file:
        img_dec = decode(file)
        if len(img_dec):
            print(img_dec[0].data.decode('utf-8'))
        else:
            print("Error: no QR Code detected in the image", file=sys.stderr)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    exit(2)
