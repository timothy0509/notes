---
tags:
  - ict
  - compulsory
  - networking
  - internet
aliases:
  - Networking Basics
  - Compulsory C1
  - Internet Protocols
---

# Networking and Internet Basics

## Computer Network

- A computer network is an interconnection of computers and peripheral devices.
- The purpose of computer networks is to exchange information and share hardware and software resources.

## Client-Server Network

- In a client-server network, a centralised administrative system (known as server) is present.
- All resources are stored in a server and shared among the clients connected to it.
- Server provides specific network services for other devices.
- Devices that request specific services from the server are called clients.

## Peer-to-Peer (P2P) Networks

- In a peer-to-peer network, all users share their files on their own.
- They can connect with and make requests directly to one another using dedicated software.

## LAN and WAN

- A **Local Area Network (LAN)** is a network that covers a small geographical area such as home or small offices.
- A **Wide Area Network (WAN)** is a network that consists of many LANs and covers a large geographical area, such as districts and countries.

| Feature | LAN | WAN |
| :--- | :--- | :--- |
| Coverage | Small | Large |
| Setup Cost | Low | High |
| Data Transfer Rate | High | Low |

## Client-Server vs Peer-to-Peer Networks

> [!success] Client-Server - Pros
> - More secure as better user management by server administrator
> - Easier to maintain the consistency of the versions of resources
> - Easier to back up and recover data

> [!failure] Client-Server - Cons
> - Higher server setup and maintenance costs
> - More difficult to set up and maintain
> - Service will stop once the server is down

> [!success] Peer-to-Peer - Pros
> - Lower cost (no need to set up a server)
> - Easier to set up as no server knowledge involved
> - Higher flexibility to add or remove devices

> [!failure] Peer-to-Peer - Cons
> - Less secure as no centralised management
> - Dedicated software is required
> - More difficult to control the versions of resources as they are distributed to different computers

## Common Network Services

- Internal Communications
- Conferencing
- Resource Sharing
  - File sharing
  - Hardware sharing
  - Software sharing
  - Internet access service sharing

## Network Interface Card (NIC)

- The NIC allows devices to communicate over a network, either using cables or wirelessly.
- Ethernet NICs are equipped with a slot for an Ethernet cable.
- Wireless NICs are commonly equipped with antennae, which help to improve signal reception.
- Each NIC has a 48-bit unique **Media Access Control (MAC)** address, which is used to identify a device connected to a network.
- A MAC address is assigned by device manufacturers and stored in the hardware.

## Switch

- A switch connects devices to form a LAN and directs incoming data to destination devices based on their MAC address.
- Data buffering (data caching) in a switch prevents data collision.

## Access Point (AP)

- It is a device that connects directly to a wired LAN (normally Ethernet).
- It provides wireless connection to other devices through Wi-Fi or other media to form a wireless LAN (WLAN).
- Each AP is identified by its **SSID** name.
- If the encryption of the AP is enabled, a data encryption key (password) will be required to connect it.
- A network administrator can limit the maximum number of concurrent users that can connect to the AP to control the network traffic and ensure decent performance of the wireless network.

## Roaming

- To achieve Wi-Fi roaming, all APs in the same network should have the same SSID.
- When a wireless device moves from the coverage area of one AP to the coverage area of another AP, the wireless NIC will disconnect from the original AP and connect to the other AP automatically.
- With roaming, the wireless connection is seamlessly switched from one to another.

## Router

- A router connects LANs with each other or connects a LAN with a WAN.
- It forwards incoming data to destination devices based on the IP address.

## Modem

- Modem, which stands for modulator-demodulator, is a device usually provided by Internet Service Providers for Internet connection.
- It is used to convert between the analog signals from the Internet and the digital signal from computers.

## Network Cables

Different cables are used to carry network signals:

| Network Cable | Pros | Cons |
| :--- | :--- | :--- |
| UTP cable | Lower cost; Easier to install | Short distance (<100m); Affected by EMI |
| STP cable | Faster than UTP; Less affected by EMI | Higher cost than UTP; Short distance (<100m) |
| Fibre optic cable | Fastest speed; Not affected by EMI; Less distance restriction; Thinner and lighter | Highest cost; Hard to install; Vulnerable to mechanical damage |

## Satellite

- Satellite can cover and build a network connection in remote areas where wired connection is not accessible.
- The installation cost and monthly subscription fees of a satellite is extremely expensive.
- The connection stability can be affected by bad weather such as rainstorms, windstorms and sunspot activities.

## Microwave

- A straight connection (line of sight) between a microwave terminal and the access point installed on the top of the building has to be established.
- The stability of microwave communication is easily affected by the weather.

## Wi-Fi

- Wi-Fi is a wireless data transmission technology based on IEEE 802.11 standards.
- Obstacles such as thick walls may greatly reduce the coverage range.

| Feature | 2.4 GHz | 5 GHz |
| :--- | :--- | :--- |
| Speed | Slower | Faster |
| Range | Longer | Shorter |
| Radio Interference | More | Less |

## Bluetooth

- Bluetooth is commonly used for short-distance wireless data transmission between mobile devices.
- Bluetooth is extremely popular due to its convenience and high compatibility.

## 5G Mobile Data and Wi-Fi 6

- 5G and Wi-Fi 6 provide us with higher data transfer rate to support newly developed applications. They also connect more users and devices to increase the network capacity.

---

# Methods of Internet Access

- An **Internet Service Provider (ISP)** is a company that provides services for accessing the Internet.

| Method | Connectivity | Bandwidth | Cost | Security | Availability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Broadband connection | Wired | High | Moderate | High | High |
| Leased Line | Wired | Highest | Highest | Highest | Moderate |
| Mobile Data | Wireless | High (5G) | High (5G) | High | High |
| Wi-Fi hotspot | Wireless | Moderate | Low | Lowest | Low |

---

# Internet Protocols

## 1. Data Transmission (TCP/IP)

- **Data division:** Data is divided into packets and numbering is added to each packet.
- **Use of IP address:** Adding the source and destination address to each packet.
- **Routing:** Select the best path to destination or an alternative path to avoid network congestion.
- **Reassembling of packets:** Data is reassembled when all packets arrive at the destination.

## 2. Addressing and Naming

### Internet Protocol (IP) Address

Numerical addresses used to identify a device in a network.

- **IPv4:** e.g., `148.7.52.1`
- **IPv6:** e.g., `2025:1ab1:1025:20b5:a19a:a315:1212`

### Fully Qualified Domain Name (FQDN)

A domain name is a human-readable and meaningful form of an IP address.

Structure (e.g., `www.google.com`):

- `www` - Hostname
- `google` - Registration name
- `com` - Top-level domain (TLD)

### DNS Server

- Used to translate domain names into IP addresses.
- This process is called ==name resolution==.
- Example: `www.google.com.hk` $\rightarrow$ [DNS Server] $\rightarrow$ `172.217.174.195`

### Uniform Resource Locator (URL)

Used to identify a specific location of a resource on the Internet.

Example: `http://www.example.hk:80/about/network.html`

| Component | Value | Description |
| :--- | :--- | :--- |
| Protocol | `http://` | Network Protocol |
| FQDN | `www.example.hk` | Fully Qualified Domain Name / IP Address |
| Port | `:80` | Port Number |
| Path | `/about/network.html` | Path |

## 3. Application Protocols

### HyperText Transfer Protocol (HTTP)

Used by the WWW to transfer hypertext documents (web pages).

| Feature | HTTP | HTTPS |
| :--- | :--- | :--- |
| URL begins with | `http://` | `https://` |
| Default port number | 80 | 443 |
| Encryption | No | Yes |
| Security | Unsecure | Secure |

### Email Protocols

- **Simple Mail Transfer Protocol (SMTP):** Used to send emails to email server.
- **Email Access Protocols (IMAP/POP3):** Used by email clients to retrieve emails from an email server.

| Feature | POP3 | IMAP |
| :--- | :--- | :--- |
| Email storage | Downloaded to local computer | Kept on the server |
| Organization | Cannot be organised on server, only on local computer | Can be organised on server; synchronised across devices |
| Internet access | Not required to read downloaded emails | Required to read emails |

> [!important] Key Point
> HTTP, SMTP, POP, and IMAP are all application protocols running on top of TCP/IP.

> [!warning] Common Misconceptions
> - POP3 clients have the option to keep emails on the server (they are not automatically removed by default).
> - Web-based email services (like Google/Yahoo) use HTTP/HTTPS protocol to send mail to the browser, not POP3/IMAP.

---

# Internet Services and Applications

## Cloud Computing, IoT, and Smart City

- **IoT:** A network connecting different objects.
- **Cloud Computing:** Used to store and process a huge amount of data generated by IoT.
  - **Operating system:** Run tasks on more powerful virtual machines.
  - **Storage:** Store data in remote servers hosted by a third party.
  - **Hosted application:** Open and use a software application from the cloud server.

## Advanced Email Features

The three recipients' fields function differently to protect personal data:

| Field | Feature | Application |
| :--- | :--- | :--- |
| **To** | The original email | Require the main recipient(s) to take action or pay attention |
| **Cc** | Addresses appear in the received header; other recipients see that a copy was sent | Send a copy for the recipients' information only |
| **Bcc** | Hides the email address; other recipients will NOT know a copy was sent to these addresses | Send a copy without letting recipients know who else is receiving the message |

## Remote Logon and Online Chat

- **Remote logon (Remote access):** Method to remotely access a device with another device. Software is usually cross-platform.
- **Online chat:** Enables private conversation (individual or group) using multimedia (text, audio, images, videos).
- **Discussion forums:** Online platforms where people can ask/answer questions or share content related to a topic.

## File Transfer

| Method | File Formats | Size Limit | Encryption |
| :--- | :--- | :--- | :--- |
| Instant messaging | Auto compression | Small | Usually end-to-end |
| Email | No restrictions | Small | Only when providers support it |
| Cloud storage | No restrictions | Large | Yes |
| Network drive/VPN | No restrictions | Limit based on local storage | No |
| P2P sharing | No restrictions | Limit based on local storage | Varies (security relatively low) |

## Web Components

### Information Search

- **Search engines:** Used for searching information on the WWW.
- **Evaluation:** Important to evaluate reliability, credibility, and timeliness.

| Search Technique | Operator | Example |
| :--- | :--- | :--- |
| Exclude results | `-` in front of keyword | `apple -fruit` |
| Combine keywords | `OR` | `mandarin orange OR tangerine` |
| Exact match | Quotations (`""`) | `"artificial intelligence"` |
| Specific website | `site:` | `site:gov.hk` |

### Multimedia and Plug-ins

- **Multimedia:** To ensure faster loading, it is important to reduce file size.
- **Common file formats:**
  - Image: JPG, PNG, GIF, APNG, WebP, SVG
  - Audio: MP3, AAC, OGG
  - Video: MP4, WebM
- **Plug-in (Add-on/Extension):** Programs that extend browser/OS functionality (codecs, etc.).
- **Media players:** Software for playback of audio/video files (online or offline).

## Streaming and Real-time Communication

### Streaming

Technology for delivering media over the Internet with a continuous flow of data (user plays/downloads simultaneously).

### Factors Affecting Streaming Quality

Media format, codec, bitrate, resolution, frame rate, network bandwidth, Internet connection.

### Communication Tools

| Feature | Video Conferencing | Webcasting |
| :--- | :--- | :--- |
| Audience size | Hundreds or relatively small | Unlimited or fairly large |
| Streaming media | Real-time | Real-time or pre-recorded |
| Communication | Two-way; more interaction | Mainly one-way; live stream comments allowed |
| Privacy | Suitable for private events | Suitable for public events |

> [!note] Voice Mail
> Real-time communication like phone calls; voice messaging is an alternative to text.

---

## Related

- [[ICT Index]] - Subject overview
- [[Compulsory C2]] - Web authoring and network security
- [[D]] - Problem formulation and programming
