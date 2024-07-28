# Advanced Cybersecurity Toolkit

## Project Overview

The **Advanced Cybersecurity Toolkit** is a powerful command-line tool designed for penetration testers and cybersecurity professionals. It includes features for wordlist generation, brute force attacks using Hydra, WiFi handshake cracking, and various advanced functionalities like reverse shell payload generation, IP tracing, and more.

## Features

- **Wordlist Generation**: Create custom wordlists for password cracking.
- **Hydra Attack**: Perform brute force attacks using Hydra with single or multiple usernames.
- **WiFi Handshake Cracking**: Crack WiFi handshakes using `aircrack-ng`.
- **Advanced Mode**: Includes additional tools such as reverse shell payload generator, IP tracer, Ducky Script encoder, and more.
- **WiFi Mode**: Scan and list available WiFi networks with details.
- **System Information**: Display system information of the target.

## Prerequisites

- **Hydra**
- **aircrack-ng**
- **ipinfo**
- **pywifi**

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/advanced-cybersecurity-toolkit.git
cd advanced-cybersecurity-toolkit
```

Install the required packages:

```bash
python install_packages.py
```

## Usage

Run the main script to start the toolkit:

```bash
python main.py
```

### Features Breakdown

#### 1. Generate Wordlist

Create a custom wordlist based on provided keywords, date ranges, and patterns.

#### 2. Perform Hydra Attack

Brute force attacks using Hydra with options for single or multiple usernames and various protocols.

#### 3. Crack WiFi Handshake

Crack WiFi handshakes using `aircrack-ng` and a wordlist.

#### 4. Advanced Mode

Additional tools including:
- **Reverse Shell Payload Generator**
- **IP Tracer**
- **Ducky Script Encoder**
- **PS1 Payload Generator**
- **WiFi Mode**
- **System Information**

### Advanced Mode

To access advanced features, select the "Advanced Mode" option from the main menu. This includes reverse shell payload generation, IP tracing, WiFi mode, and more.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
