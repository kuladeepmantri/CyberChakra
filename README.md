# CyberChakra

## About

I am pleased to introduce my personal port scanning tool, CyberChakra. Built on top of Nmap, this tool is designed to meet all of my security-related needs such as CTF challenges and penetration testing. With threading and logging functionality, CyberChakra allows me to work efficiently while also providing a detailed record of its activity. I am also excited to announce that I am currently working on implementing machine learning techniques to improve the accuracy of port prediction. While it may not be perfect, CyberChakra has proven to be a reliable and valuable asset in my toolkit. I hope you enjoy using it as much as I do!

## Usage

To use this program, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/kuladeepmantri/CyberChakra.git
```

2. Navigate to the repository folder:

```bash
cd repo
```

3. Run the program with Python:

```bash
python cyberchakra.py
```

4. Enter the IP address or URL to scan when prompted.

5. Optionally, you can also enter the number of threads and port range to scan.

6 . The program will scan the specified ports and display the results.

## Requirements

- Python 3.5 or later
- nmap command-line tool

## Installation

### Install Python

If you don't already have Python installed, you can download it from the [official website](https://www.python.org/downloads/).

### Install nmap

Windows

1. Download the nmap installer from the [official website](https://nmap.org/download.html#windows).

2. Run the installer and follow the instructions.

3. Add the nmap directory to your PATH environment variable.


macOS

1. Install Homebrew by running the following command in the terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Install nmap by running the following command in the terminal:

```bash
brew install nmap
```

Linux

1. Install nmap by running the following command in the terminal:

```bash
sudo apt-get install nmap
```

## License

[MIT License](https://choosealicense.com/licenses/mit/)
