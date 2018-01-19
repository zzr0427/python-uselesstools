from setuptools import setup, find_packages

setup(
    name="UselessTools",  # pypi中的名称，pip或者easy_install安装时使用的名称，或生成egg文件的名称
    version="0.1",
    author="ZHENG Zongrong",
    author_email="zzr0427@163.com",
    description=("A userless python toolkit"),
    packages=find_packages('uselesstools'),
    package_dir={'': 'uselesstools'},
    zip_safe=False,  # 此项需要，否则卸载时报windows error
    # install_requires=[
    #     'Werkzeug>=0.9',
    # ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
    ],
)
