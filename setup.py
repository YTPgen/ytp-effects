import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as r:
    requirements = r.readlines()

setuptools.setup(
    name="ytp-effects",  # Replace with your own username
    version="0.0.1",
    author="Karl Gylleus",
    author_email="karl.gylleus@gmail.com",
    description="YTP effects for images and audio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[requirements],
    dependency_links=[
        "https://github.com/YTPgen/face-feature-recognizer/tarball/master#egg=face_feature_recognizer-0.0.1"
    ],
    python_requires=">=3.6",
)
