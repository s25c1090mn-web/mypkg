from setuptools import find_packages, setup

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
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fukuisakuya',
    maintainer_email='fukuisakuya@todo.todo',
    description='a package for practice',
    license='BSD-3-Claus',
    extras_require={
        'test': [
            'pytest',
        ],
    },
 entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',      #talker.pyのmain関数をtalkerという名前で
            'listener = mypkg.listener:main', #後で使うので書いておいてコメントアウト
        ],
    },
)
