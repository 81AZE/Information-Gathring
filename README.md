# OSINT Automation Tool Readme

## Overview
This technical readme provides information about an Open Source Intelligence (OSINT) automation tool designed for domain investigation. The tool takes a domain as input and offers capabilities to retrieve WHOIS information, DNS records, geolocation data, and Shodan search information. Additionally, it allows users to save the output to a file by specifying a filename using the `-o` option.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
    - [Command Line Options](#command-line-options)
4. [Output](#output)
5. [Contributing](#contributing)
6. [License](#license)

## Prerequisites
Before using the OSINT automation tool, make sure you have the following prerequisites:

- Python 3.x
- The required Python packages, which can be installed via `pip`:
    - `requests` for making HTTP requests
    - `socket` for DNS queries
    - `python-whois` for WHOIS information
    - `geopy` for geolocation data
    - `shodan` for Shodan search

## Installation
To set up the tool, follow these steps:

1. Clone the repository to your local machine or download the source code.

```bash
git clone https://github.com/yourusername/osint-automation-tool.git
```

2. Navigate to the project directory:

```bash
cd osint-automation-tool
```

3. Install the required Python packages using `pip`:

```bash
pip install requests python-whois geopy shodan
```

## Usage
To utilize the OSINT automation tool, adhere to these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where you installed the tool.

3. Run the tool with the following command:

```bash
python osint_tool.py -d example.com
```

### Command Line Options
- `-d` or `--domain`: Specify the domain you want to investigate.
- `-o` or `--output`: Optional. Specify a filename to save the output. If not specified, the output will be displayed in the terminal.
- `-h` or `--help`: Display help and usage information.

## Output
The tool provides information on the specified domain in the following categories:

1. **WHOIS Information**: Includes details about the domain's registration, owner, and contact information.

2. **DNS Records**: Provides information about the domain's DNS records, including A, MX, NS, and SOA records.

3. **Geolocation Data**: Offers geographic information about the IP address associated with the domain.

4. **Shodan Search Info**: Gathers information from Shodan, including open ports, services, and potential vulnerabilities.

The tool will display the results in the terminal by default. To save the output to a file, use the `-o` option:

```bash
python osint_tool.py -d example.com -o output.txt
```

## Contributing
Contributions to this project are encouraged. You can contribute by:

- Reporting issues or bugs
- Suggesting enhancements or new features
- Submitting pull requests with improvements

Please follow the project's guidelines for contributions and adhere to the code of conduct.

## License
This tool is open source and is distributed under the [MIT License](LICENSE). You are free to use, modify, and distribute it in accordance with the terms of the license.