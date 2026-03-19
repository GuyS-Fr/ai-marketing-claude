from setuptools import setup, find_namespace_packages

setup(
    name="cli-anything-aimarketing",
    version="0.1.0",
    description="CLI harness for ai-marketing-claude — AI-powered marketing analysis and content generation",
    author="cli-anything",
    python_requires=">=3.6",
    packages=find_namespace_packages(include=["cli_anything.*"]),
    install_requires=[
        "click>=7.0",
    ],
    extras_require={
        "pdf": ["reportlab>=4.0"],
    },
    entry_points={
        "console_scripts": [
            "cli-anything-aimarketing=cli_anything.aimarketing.aimarketing_cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
