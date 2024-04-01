# central-server


## Setup Instructions

### Creating a Virtual Environment

To isolate our project dependencies, we'll create a virtual environment. Open your terminal and run the following command in the project directory:

```bash
python3 -m venv venv
```

This command creates a virtual environment named `venv`. 

### Activating the Virtual Environment

Before installing the project dependencies, activate the virtual environment with:

- **On Windows:**

```cmd
.\venv\Scripts\activate
```

- **On macOS and Linux:**

```bash
source venv/bin/activate
```

### Installing Project Dependencies

With the virtual environment activated, install the project dependencies using:

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file and installs all the listed packages.

---
