from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shelter',
    maintainer_email='sansbook@icloud.com',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'year_count = mypkg.year_count:main',
        ],
    },
)
