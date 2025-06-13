# UserFoot - OSINT Username Checker

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

UserFoot is a simple yet powerful OSINT tool that checks the existence of a username across multiple popular websites and social media platforms. It helps investigators, security researchers, and curious individuals to quickly identify where a particular username is being used.

## Features

- Checks 35+ popular websites and platforms
- Simple web interface with Bootstrap styling
- Quick results with status indicators
- Direct links to found profiles
- Lightweight Flask backend
- Easy to deploy and extend

## Screenshot

![UserFoot Screenshot](screenshot.png)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/userfoot.git
cd userfoot
```

Install the required dependencies:

```bash
pip install flask requests
```

Run the application:

```bash
python app.py
Open your browser and navigate to http://localhost:5000
```

# Usage
Enter a username in the search box

Click "Check"

View results:

Green "Found" button indicates the username exists (click to visit)

Red "Not Found" badge indicates the username wasn't found

Supported Platforms
UserFoot currently checks these platforms:

- GitHub, GitLab, Bitbucket

- Social Media: Twitter, Instagram, Facebook, etc.

- Tech Communities: Stack Overflow, LeetCode, HackerRank

- Creative Platforms: DeviantArt, Dribbble, Behance

- Gaming: Steam, Twitch, Xbox

- And many more...


# Disclaimer
This tool is intended for legal and ethical use only. Always respect privacy and terms of service of the platforms you're checking.
