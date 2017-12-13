from setuptools import setup, find_packages

setup(
    name='DontWannaTalk server',
    version='0.1',
    description='Server application for DontWannaTalk chat',
    long_description='JIM-based chat built with Python 3 and PyQt5',
    author='Nikolay Moroz',
    author_email='ndmoroz@gmail.com',
    url='https://github.com/ndmoroz/dont-wanna-talk',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Communications :: Chat',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English'
    ],
    keywords=['Python', 'Python3', 'PyQt', 'PyQt5', 'JIM', 'chat'],
    packages=find_packages('fb_server'),
    package_dir={'': 'fb_server'},
    install_requires=[
        'SQLAlchemy',
        'PyQt5'
    ],
    entry_points={
        'console_scripts': [
            'finger_server=fb_server.main:main',
        ],
    },
)
