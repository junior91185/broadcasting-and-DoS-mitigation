# Broadcasting and DoS Mitigation

## Overview

This project was developed as part of a hands-on lab for *Introduction to Cryptography and Computer Security. It demonstrates:
- Client-server communication using UDP.
- Broadcasting messages from the client to the server.
- Implementation of DoS (Denial of Service) mitigation strategies.

This lab provided an opportunity to apply networking principles in a practical setting, showcasing skills in socket programming, multithreading, and DoS mitigation techniques.

---

## Features

- **Client-Server Communication**:
    - Clients broadcast UDP messages to the server
    - The server listens for broadcasts and responds dynamically to clients
- **Anti-DoS Strategies**:
  - Rate-limiting requests per client
  - Blacklisting abusive clients
  - Multithreaded request handling for scalability

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/junior91185/broadcasting-and-DoS-mitigation.git
   cd broadcasting-and-DoS-mitigation
   python3 code/server_ReceiveBroadcast.py
   python3 code/client_broadcasting_loop.py

