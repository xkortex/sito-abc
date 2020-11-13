from setuptools import setup, find_packages


pkgname = 'sito-abc'

deps = [
    'six',
    'typing',
]

packages = find_packages(include=['sito_abc'])

setup(
    name=pkgname,
    use_scm_version={
        'write_to': 'sito_abc/_version.py',
        'write_to_template': '__version__ = "{version}"',
    },
    script_name='setup.py',
    python_requires='>2.7',
    zip_safe=True,
    setup_requires=['setuptools_scm'],
    install_requires=deps,
)
