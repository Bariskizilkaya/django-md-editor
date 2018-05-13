from setuptools import setup

setup(
    name="django-md-editor",
    version='0.0.3',
    description='djmd package helps integrate editor.md with Django.',
    long_description=open('README.md').read(),
    author='hakancelik96',
    author_email='hakancelik96@outlook.com',
    packages=["djmd"],
    include_package_data=True,
    install_requires=[],
    url="https://github.com/coogger/django-md-editor",
    license='MIT',
    zip_safe=False,
    keywords='editor.md,django,editor,text,editor,rich,markdown,md',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
