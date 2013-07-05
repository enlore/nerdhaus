from setuptools import setup

setup(
       name='nerdhaus',
       version='1.0.',
       long_description=__doc__,
       packages=['nerdhaus'],
       include_package_data=True,
       zip_safe=False,
       install_requires=[
            'Flask==0.10.1',
            'Jinja2==2.7',
            'MarkupSafe==0.18',
            'Werkzeug==0.9.1',
            'argparse==1.2.1',
            'distribute==0.6.34',
            'gunicorn==17.5',
            'itsdangerous==0.21',
            'wsgiref==0.1.2'
           ]
       )
