from setuptools import setup, find_packages

setup(
    name='chopmon',
    description='Chopmon is a monitoring tool which uses the Chopsicks orchestration library.',
    long_description=open('README.rst').read(),
    version="0.0.1",
    author='Salim Fadhley',
    author_email='sal@stodge.org',
    url='',
    packages=find_packages(),
    zip_safe=False,
    install_requires=["chopsticks"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: System :: Systems Administration'
    ]
)