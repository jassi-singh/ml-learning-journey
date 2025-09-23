# ML Learning Journey

A comprehensive machine learning learning journey covering fundamental concepts from NumPy basics to advanced regression techniques.

## 📁 Project Structure

```
ml-learning-journey/
├── 📁 notebooks/                    # All Jupyter notebooks organized by topic
│   ├── 📁 01_numpy_basics/         # NumPy fundamentals
│   │   └── numpy_basics.ipynb
│   ├── 📁 02_linear_regression/    # Linear regression implementations
│   │   ├── 01_simple_linear_regression.ipynb
│   │   └── 02_multivariate_linear_regression.ipynb
│   └── 📁 03_scikit_learn/         # Scikit-learn implementations
│       └── multivar_regression_sklearn.ipynb
├── 📁 src/                         # Source code and utilities
│   ├── 📁 utils/                   # Utility functions
│   │   ├── common_utils.py         # Common ML utilities
│   │   ├── univariate_utils.py     # Univariate regression utilities
│   │   └── plotting_utils.py       # Plotting and visualization utilities
│   └── 📁 models/                  # Model implementations
├── 📁 data/                        # Data files
│   ├── raw/                        # Original data files
│   │   └── housing_data.txt
│   └── processed/                  # Processed/cleaned data
├── 📁 config/                      # Configuration files
│   └── matplotlib_styles/
│       └── deeplearning.mplstyle
├── 📁 docs/                        # Documentation
├── 📁 tests/                       # Test files
└── 📁 requirements/                # Dependencies
    └── requirements.txt
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Conda (recommended) or pip
- Jupyter Notebook or JupyterLab

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd ml-learning-journey
```

2. Create and activate conda environment:

```bash
conda create -n ml_env python=3.9
conda activate ml_env
```

3. Install dependencies:

```bash
conda install --file requirements/requirements.txt
```

4. Start Jupyter:

```bash
jupyter notebook
```

## 📚 Learning Path

### 1. NumPy Basics (`notebooks/01_numpy_basics/`)

- Array creation and manipulation
- Basic operations and broadcasting
- Indexing and slicing

### 2. Linear Regression (`notebooks/02_linear_regression/`)

- **Simple Linear Regression**: Basic implementation with gradient descent
- **Multivariate Linear Regression**: Multiple features implementation

### 3. Scikit-learn (`notebooks/03_scikit_learn/`)

- Using industry-standard libraries
- Model evaluation and comparison

## 🛠️ Utilities

The `src/utils/` directory contains reusable utility functions:

- **`common_utils.py`**: Core ML functions (cost computation, gradient calculation)
- **`univariate_utils.py`**: Visualization functions for univariate regression
- **`plotting_utils.py`**: General plotting and visualization utilities

## 📊 Data

- **`data/raw/housing_data.txt`**: California housing dataset for regression examples

## 🎨 Configuration

- **`config/matplotlib_styles/deeplearning.mplstyle`**: Custom matplotlib styling for consistent visualizations

## 📝 Learning Notes

This project follows a structured learning approach:

1. **Foundation**: Start with NumPy basics
2. **Implementation**: Build models from scratch
3. **Libraries**: Use industry-standard tools
4. **Practice**: Apply concepts to real datasets

## 👨‍💻 Author

**Jassi Singh** - ML Learning Journey

## 🤝 Contributing

This is a personal learning project, but suggestions and improvements are welcome!

## 📄 License

This project is for educational purposes.
