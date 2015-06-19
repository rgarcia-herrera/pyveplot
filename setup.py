from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

    
setup(name='pyveplot',
      version='0.6',
      description='SVG Hiveplot Python API',
      long_description=readme(),
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
      ],
      url='http://github.com/CSB-IG/pyveplot',
      author='Rodrigo Garcia',
      author_email='rgarcia@inmegen.gob.mx',
      license='GPLv3',
      packages=['pyveplot'],
      install_requires=[ 'svgwrite' ],
#      scripts=['bin/hiveplot.py'],
#      include_package_data=True,
      zip_safe=False)
