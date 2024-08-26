# HopsComponents
Hops components for grasshopper/ Rhino 3d

## 1. Instructions

### 1.1 Creating Python Environment

Follow the steps to create an environment and install dependancies:

#### Step 1: Create Python Environment

Create a new anaconda environment named \`hops_env\`:

```
conda create --name hops_env python=3.9
```

#### Step 3: Activate Environment

Activate the environment with:

```
conda activate hops_env
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
OR using the .yml file:
```
conda env update --file environment.yml
```