from setuptools import find_packages, setup

setup(
    # 以下为必需参数
    name='hpyculator',
    version='1.0.0',
    description='这是一个基于python的可编程计算器',
    package_dir={"": "src"},
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    long_description="这是一个基于python的可编程计算器",
    url='https://github.com/pypa/sampleproject',
    author='HowieHz', # 作者名
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

    ],
    install_requires=[
        'wxpython'
    ],
        project_urls={
        'Bug Reports': 'https://github.com/HowieHz/hpyculatorPackage/issues',
    },
)