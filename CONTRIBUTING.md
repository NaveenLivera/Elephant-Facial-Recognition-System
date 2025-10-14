# Contributing to Elephant Face ID & NFT Generation System

First off, thank you for considering contributing to this project! It's people like you that help make elephant conservation through technology a reality.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by respect, professionalism, and a shared commitment to wildlife conservation. By participating, you are expected to uphold this standard.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (screenshots, code snippets)
- **Describe the behavior you observed** and what you expected
- **Include your environment details** (OS, Python version, library versions)

Example bug report:

```markdown
**Title:** Face detection fails on images with multiple elephants

**Description:** 
When processing images containing more than one elephant, the system 
only detects the first elephant and ignores the others.

**Steps to Reproduce:**
1. Run `system.process_image("multi_elephant.jpg")`
2. Observe only one detection result

**Expected Behavior:** 
System should detect all elephants in the image

**Environment:**
- OS: Windows 10
- Python: 3.9.7
- OpenCV: 4.5.3
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **List any alternatives** you've considered

### Contributing Code

#### Good First Issues

Look for issues tagged with `good first issue` - these are great for newcomers!

#### Priority Areas

1. **Deep Learning Integration**
   - Implement CNN-based face detection
   - Add transfer learning capabilities
   - Improve feature extraction with pre-trained models

2. **Performance Optimization**
   - GPU acceleration support
   - Batch processing improvements
   - Memory optimization

3. **Testing**
   - Unit tests for all modules
   - Integration tests
   - Performance benchmarks

4. **Documentation**
   - API documentation
   - Tutorial notebooks
   - Video tutorials

5. **Blockchain Integration**
   - Smart contract implementation
   - IPFS upload functionality
   - Wallet integration

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/elephant-face-id-nft.git
cd elephant-face-id-nft
```

### 2. Create Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Using conda
conda create -n elephant-id python=3.9
conda activate elephant-id
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development tools
```

### 4. Create Development Branch

```bash
git checkout -b feature/your-feature-name
```

## Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications:

- **Line length**: 100 characters (not 79)
- **Indentation**: 4 spaces
- **Quotes**: Double quotes for strings
- **Imports**: Group standard library, third-party, and local imports

### Code Structure

```python
# Good: Clear, documented, modular
def detect_elephant_face(image, min_size=50, method="contour"):
    """
    Detect elephant face in image using specified method.
    
    Args:
        image (np.ndarray): Input image in BGR format
        min_size (int): Minimum face size in pixels
        method (str): Detection method ('contour', 'edge', 'both')
    
    Returns:
        list: List of face rectangles (x1, y1, x2, y2)
    
    Raises:
        ValueError: If method is invalid
    """
    if method not in ["contour", "edge", "both"]:
        raise ValueError(f"Invalid method: {method}")
    
    # Implementation...
    return face_rects
```

### Docstring Format

Use Google-style docstrings:

```python
def function_name(param1, param2):
    """
    Brief description of function.
    
    Longer description if needed, explaining the purpose
    and behavior of the function.
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
    
    Returns:
        type: Description of return value
    
    Raises:
        ExceptionType: When this exception occurs
    
    Example:
        >>> function_name("test", 42)
        "result"
    """
    pass
```

### Variable Naming

- **Classes**: `PascalCase` (e.g., `ElephantFaceID`)
- **Functions/Methods**: `snake_case` (e.g., `extract_features`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `DEFAULT_THRESHOLD`)
- **Private**: Prefix with underscore (e.g., `_internal_method`)

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, semicolons, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

#### Examples

```bash
# Good commits
feat(detection): add CNN-based face detection method
fix(matching): correct cosine similarity calculation
docs(readme): update installation instructions
test(features): add unit tests for texture extraction

# Bad commits
update stuff
fixed bug
changes
```

### Commit Best Practices

- **One logical change per commit**
- **Write clear, descriptive messages**
- **Reference issues** when applicable (#123)
- **Keep commits atomic** and reversible

## Pull Request Process

### Before Submitting

- [ ] Code follows the style guidelines
- [ ] All tests pass locally
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] No merge conflicts
- [ ] Commit history is clean

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How has this been tested?

## Screenshots (if applicable)
Add screenshots to help explain your changes

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where needed
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
- [ ] New and existing tests pass locally
```

### Review Process

1. **Automated Checks**: CI/CD must pass
2. **Code Review**: At least one maintainer approval required
3. **Testing**: Manual testing for significant changes
4. **Documentation**: Verify docs are updated
5. **Merge**: Squash and merge preferred

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_detection.py

# Run with coverage
pytest --cov=elephant_face_id
```

### Writing Tests

```python
import pytest
from elephant_face_id import ElephantFaceID

def test_face_detection_single_elephant():
    """Test face detection on image with single elephant."""
    system = ElephantFaceID()
    image = load_test_image("single_elephant.jpg")
    
    faces = system.detect_elephant_face(image)
    
    assert len(faces) == 1
    assert faces[0][2] - faces[0][0] > 50  # Width check

def test_face_detection_no_elephant():
    """Test face detection on image without elephant."""
    system = ElephantFaceID()
    image = load_test_image("landscape.jpg")
    
    faces = system.detect_elephant_face(image)
    
    assert len(faces) == 0
```

## Documentation

### Updating Documentation

- Update README.md for new features
- Add docstrings to all public functions
- Create tutorials for complex features
- Update API documentation

### Documentation Tools

```bash
# Generate API documentation
pdoc3 --html --output-dir docs elephant_face_id

# Serve documentation locally
cd docs && python -m http.server 8000
```

## Questions?

Feel free to reach out:

- **GitHub Discussions**: For questions and ideas
- **GitHub Issues**: For bugs and feature requests
- **Email**: your.email@example.com

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing to elephant conservation through technology! 🐘
