from setuptools import setup, find_packages
from mtcnn import __version__ as VERSION

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'opencv-contrib-python>=4.5.4.60',
    'tensorflow==2.9.1',
]

test_requirements = [
]

setup(
    name                = 'mtcnn-python',
    version             = VERSION,
    description         = 'mtcnn-python package.',
    long_description    = readme,
    url                 = 'https://github.com/leeyunjai/mtcnn-python',
    packages            = find_packages(),
    package_data                = {'' : ['data/*']},
    include_package_data        = True,
    zip_safe                    = False,
    install_requires    = requirements,
    keywords            = 'mtcnn',
    classifiers         = [
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite          = 'tests',
    tests_require       = test_requirements
)
