from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="elephant-face-id-nft",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Elephant face identification system with NFT generation capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/elephant-face-id-nft",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/elephant-face-id-nft/issues",
        "Documentation": "https://github.com/yourusername/elephant-face-id-nft#readme",
        "Source Code": "https://github.com/yourusername/elephant-face-id-nft",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "opencv-python>=4.5.0",
        "numpy>=1.19.0",
        "scikit-learn>=0.24.0",
        "scipy>=1.6.0",
        "Pillow>=8.0.0",
        "matplotlib>=3.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.10",
            "black>=21.0",
            "flake8>=3.9",
            "mypy>=0.900",
            "pdoc3>=0.9",
        ],
        "gpu": [
            "opencv-contrib-python>=4.5.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "elephant-id=elephant_face_id_nft:main",
        ],
    },
    keywords=[
        "elephant",
        "face-recognition",
        "wildlife-conservation",
        "computer-vision",
        "nft",
        "blockchain",
        "identification",
        "opencv",
        "machine-learning",
    ],
    include_package_data=True,
    zip_safe=False,
)
