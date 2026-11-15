# Mission 7 — Computer networks

## 1. Task / objective
Explain common network terms, check website reachability and DNS lookup, and describe how a browser requests a website.

## 2. Work completed

### Network concepts
- **LAN:** Local Area Network; connects devices in a limited area such as a home, lab or office.
- **MAN:** Metropolitan Area Network; connects networks across a town or city.
- **WAN:** Wide Area Network; connects networks across large geographic areas.
- **DNS:** Domain Name System; finds the IP address associated with a domain name.
- **Router:** forwards network traffic between networks.
- **Protocol:** agreed rules for communication, such as HTTP, HTTPS or TCP.
- **Packet switching:** breaks data into packets that can travel across networks and be reassembled.
- **Client-server:** a client requests a service or resource; a server responds.

### Safe practical checks on macOS
Run these in Terminal and record only whether the lookup/reachability succeeded and a brief general observation. Do not publish your own IP address or network details.

```bash
ping -c 4 example.com
nslookup example.com
```

My actual observations: `[FILL IN; redact IP addresses and private network information]`.

### How a website request works (7 steps)
1. I enter a website name in the browser.
2. The computer checks whether it already knows the domain's address.
3. DNS resolves the domain name to an IP address.
4. The browser establishes a connection to the server.
5. For HTTPS, the connection is secured using TLS.
6. The browser sends an HTTP request and the server sends a response.
7. The browser processes the response and displays the webpage.

## 3. Commands / tools used
`ping -c 4 example.com`, `nslookup example.com`, and a web browser. `[VERIFY and record actual results]`.

## 4. My understanding
A network allows devices to exchange data. DNS helps people use domain names instead of remembering IP addresses. Protocols define how the communication happens.

## 5. Difficulties faced
[FILL IN actual difficulties, such as a timeout or DNS lookup failure.]

## 6. How I resolved them
[FILL IN what you actually tried. Do not claim success if the network check failed.]

## 7. Evidence / files
This README contains the concepts and website-request steps. Add only privacy-safe command observations.

## 8. Commit details
Suggested commit: `Explain networking concepts and website communication`
Actual commit hash / push status: `[FILL IN]`.
