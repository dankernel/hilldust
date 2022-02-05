
from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
        name="hillstone-client",
        version="1.0.1",
        description="Simple Hillstone client for linux",
        url="https://github.com/dankernel/hilldust",
        author="dankernel, dsparch",
        author_email="dkdkernel@gmail.com",
        license="GPL3.0",
        packages=["hillstone_client"],
        zip_safe=False,
        install_requires=[
            "cryptography==36.0.1", 
            "scapy==2.4.5"
        ],
        scripts=["hillstone_client/hillstone-client"],
        python_requires='>=3.8',
        long_description=long_description,
        long_description_content_type='text/markdown'
)





