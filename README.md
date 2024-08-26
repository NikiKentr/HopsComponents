# HopsComponents
Hops components for grasshopper/ Rhino 3d

## 1. Instructions

### 1.1 Creating Python Environment

Follow the steps to create an environment and install dependancies:

#### Step 1: Install Python Environments

First, ensure that you have the \`python3-venv\` package installed. Run the following command:

```
sudo apt install python3-venv
```

#### Step 2: Create Python Environment

Create a new Python environment named \`hops_env\`:

```
python3 -m venv hops_env
```

#### Step 3: Activate Environment

Activate the environment with:

```
source hops_env/bin/activate
```

### 1.2 Clone

```
git clone https://github.com/NikiKentr/HopsComponents.git
```

### 1.3 Environment Requirements

To install the dependencies listed in ```requirements.txt``` on another machine or environment:

Install the dependencies (while environment is activated) with:

```
pip install -r requirements.txt
```