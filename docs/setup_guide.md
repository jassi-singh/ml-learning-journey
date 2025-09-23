# Setup Guide

## Environment Setup

### 1. Conda Environment

Create a conda environment:

```bash
conda create -n ml_env python=3.9
conda activate ml_env
```

### 2. Install Dependencies

```bash
conda install --file requirements/requirements.txt
```

### 3. Verify Installation

```python
import numpy as np
import matplotlib.pyplot as plt
import sklearn
print("All packages installed successfully!")
```

## Running Notebooks

### 1. Start Jupyter

```bash
jupyter notebook
```

### 2. Navigate to Notebooks

- Open `notebooks/01_numpy_basics/numpy_basics.ipynb` to start
- Follow the learning path in order

### 3. Import Path Setup

Each notebook includes the necessary path setup:

```python
import sys
import os
sys.path.append('../../src')
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure you're running notebooks from the correct directory
2. **Style Not Found**: Verify the matplotlib style file path
3. **Data Not Found**: Check that data files are in the correct location

### Getting Help

- Check the README.md for project structure
- Review the utility functions in `src/utils/`
- Ensure all dependencies are installed
