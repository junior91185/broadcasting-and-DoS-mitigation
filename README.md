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

## Screenshots and Results

### 1. Broadcasting in Action
The client broadcasts messages to the server, which listens and responds in real-time

Here, the server is listening for broadcasts

![Server Listening Results](screenshots/server_listening_results.png)

Here are the results of a successful client broadcast

![Client Broadcasting Results](screenshots/client_broadcasting_results.png)

---

### 2. DoS Mitigation in Action
Here, the server safeguards itself against excessive traffic by implementing rate limiting and blacklisting

![Anti-DoS Implementation](screenshots/anti_DoS_implementation.png)

---

### 3. Broadcasting Loop in Action
Here’s the output from a client broadcasting continuously to the server

![Broadcasting Loop](screenshots/broadcasting_loop.gif)

---
---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/junior91185/broadcasting-and-DoS-mitigation.git
   cd broadcasting-and-DoS-mitigation
   python3 code/server_ReceiveBroadcast.py
   python3 code/client_broadcasting_loop.py

