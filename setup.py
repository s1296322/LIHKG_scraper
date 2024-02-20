from setuptools import setup, find_packages

setup(
    name='LIHKG_scraper',
    version='0.1.0',
    author= 'FYP',
    author_email='yeungchoho5@gmail.com',
    description='A web scraper for LIHKG forums',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/s1296322/LIHKG_scraper',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'selenium',
        'beautifulsoup4',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)