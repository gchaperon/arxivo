import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arxivo", # Replace with your own username
    version="0.0.1",
    author="Gabriel Chaperon",
    author_email="gabrielchaperonb@gmail.com",
    description="El arXivo, but just for u ::wink:: !",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gchaperon/arxivo",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "arxivo = arxivo:main"
        ]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)