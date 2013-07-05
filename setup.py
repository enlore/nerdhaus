from setuptools import setup

def get_requirements(filename):
    """ Pull requirements from file in application root"""
    with open('requirements.txt', 'r') as f:
        lines = f.readlines()
        reqs = []
        for line in lines:
            reqs.append(line.strip())
        return reqs

setup(
       name='nerdhaus',
       version='1.0.',
       long_description=__doc__,
       packages=['nerdhaus'],
       include_package_data=True,
       zip_safe=False,
       install_requires=get_requirements('requirements.txt')
       )
