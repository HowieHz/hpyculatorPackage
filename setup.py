from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    # 以下为必需参数
    name='hpyculator',
    version='1.3.1',
    description='这是一个基于python的可编程计算器',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description=long_description,
    url='https://github.com/HowieHz/hpyculatorPackage',
    author='HowieHz', # 作者名
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

    ],
    install_requires=[
        'pyside6'
    ],
        project_urls={
        'Bug Reports': 'https://github.com/HowieHz/hpyculatorPackage/issues',
    },
)
