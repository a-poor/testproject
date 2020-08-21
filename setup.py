import setuptools

long_description = """
# Test Project

This is a test project for learning 
how to use sphinx and read-the-docs.

"""

setuptools.setup(
    name="apoor-testproject", # Replace with your own username
    version="0.0.1",
    author="Austin Poor",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a-poor/testproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)