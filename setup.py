import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ytp-effects",  # Replace with your own username
    version="0.0.1",
    author="Karl Gylleus",
    author_email="karl.gylleus@gmail.com",
    description="YTP effects for images and audio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["scikit-image"],
    python_requires=">=3.6",
)
