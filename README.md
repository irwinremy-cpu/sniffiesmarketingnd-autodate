# automaticGrindr

An automated advertising and dating platform for sniffies.com built with Python and Playwright.

## Overview

automaticGrindr is a sophisticated automation tool designed to handle both advertising campaigns and dating interactions on the sniffies.com platform. The system uses multiple browser agents to simulate real user behavior while incorporating anti-detection measures to avoid platform restrictions.

## Features

- **Multi-Agent Architecture**: Run multiple browser instances simultaneously to handle concurrent interactions
- **Anti-Detection Mechanisms**: Implement browser fingerprinting techniques to avoid detection
- **Database Integration**: Store user data and interaction history using SQLite
- **Ad Campaign Management**: Automated advertising posting and tracking
- **Dating Platform Automation**: Profile browsing, messaging, and liking functionality
- **Session Management**: Persistent browser sessions with geolocation spoofing

## Architecture

```
automaticGrindr/
├── src/
│   ├── __init__.py
│   ├── main.py              # Main application entry point
│   ├── agents.py            # Browser agent management
│   ├── interactions.py      # Interaction handling with sniffies.com
│   ├── database.py          # Data persistence layer
│   └── utils.py             # Utility functions
├── tests/
│   └── test_main.py         # Basic application tests
├── venv/                    # Virtual environment (not committed)
├── data/                    # Application data directory (not committed)
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/irwinremy-cpu/sniffiesmarketingnd-autodate.git
cd automaticGrindr
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
python -m playwright install
```

5. Install system dependencies (Ubuntu/Debian):
```bash
sudo apt-get install libavif16 libmanette-0.2-0
```

## Usage

Run the application:
```bash
python src/main.py
```

The application will:
1. Initialize multiple browser agents
2. Set up database connections
3. Start automated interactions with sniffies.com
4. Run for 10 minutes (demo duration)
5. Clean up resources upon completion

## Configuration

The application can be customized by modifying:
- Number of agents in `main.py`
- Interaction frequency in `interactions.py`
- Database storage location in `database.py`
- Browser configurations in `agents.py`

## Security Notice

This tool is intended for educational purposes only. Please ensure compliance with sniffies.com's Terms of Service and applicable laws before using this software.

## License

MIT License