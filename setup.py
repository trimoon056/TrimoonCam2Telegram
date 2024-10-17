from setuptools import setup, find_packages

setup(
    name='TrimoonCam2Telegram',
    version='0.1.1',
    author='Trimoon Cam 2 Telegram',
    author_email='trimoon056@gmail.com',
    description='Push Cam Affiliate links ',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/trimoon056/TrimoonCam2Telegram',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7, <3.13',
    install_requires=[
        'Pillow',
        'python-dotenv',
        'sockets',
        'pycountry',
        'pycountry-convert',
        'requests',
        'pyTelegramBotAPI'
    ],
)