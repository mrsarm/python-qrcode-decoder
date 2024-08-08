QR Code Decoder command line tool
=================================

`qdec.py` is a simple CLI tool written in Python to decode the payload of a QR Code image,
using `pillow` to decode the image, and `pyzbar` to decode the QR content. the payload content
is printed in the standard output. 

```shell
$ ./qdec.py --help
qdec.py: decode the payload of a QR Code image.

Usage: qdec.py <IMAGE FILE>

$ ./qdec.py qrcode-wifi.jpg 
WIFI:S:Home-WIFI;T:WPA;P:TheSecret;H:false;;
```
