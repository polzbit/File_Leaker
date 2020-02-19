# File_Leaker
Simple python project to demonstrate how to use scapy module to leak file from Client to Server.

## Getting Started

fileLeaker installed on client machine set to transfer "screen1.png" to fileServer on server machine via ICMP packets.
fileServer insralled on server machine set to receive "screen1.png" from fileLeaker.

## Deployment

Set file and run `fileLeaker.py` first on client machine, then run `fileReceiver.py` to get the file on server machine.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
