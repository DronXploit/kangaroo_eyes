from setuptools import setup, find_packages

setup(
    name="kangaroo_eyes",
    version="1.0.0",
    description="Network Reconnaissance Tool",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        'colorama',
        'python-whois',
        'python-dotenv',
        'dnspython',
        'python-nmap',  # Changed from 'nmap'
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'kangaroo-eyes = kangaroo_eyes.main:main',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)