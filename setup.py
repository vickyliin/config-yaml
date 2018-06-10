from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='config-yaml',
    version='0.0.2',
    description='Serialize and deserialize your configurations/arguments to yaml.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vickyliin/config-yaml',
    author='vickyliin',
    author_email='vickyliinn@gmail.com',
    license='MIT',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
	'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3 :: Only'
    ],

    keywords='config yaml argparse serialize experiment',
    py_modules=['configyml'], 
    install_requires=['pyyaml']
)
