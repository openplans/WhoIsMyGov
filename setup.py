try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='whoismygov',
    version='0.2',
    description='',
    author='',
    author_email='',
    url='',
    dependency_links=[
        "https://svn.openplans.org/eggs/",
        ],
    install_requires=[
        "Pylons>=0.9.7",
        "SQLAlchemy>=0.5",
        "SQLAlchemy-migrate>=0.5",
        "psycopg2",  # For PostGIS.
        "pyproj",
        "python-votesmart",
        "shapely",
        "simplejson",
        "geojson>=1.0.1",
        "geopy>=0.93dev",
        "lxml>=2.2",
        "PyYAML",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'whoismygov': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'whoismygov': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = whoismygov.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
