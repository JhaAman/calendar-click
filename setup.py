from setuptools import setup

setup(
    name='CalVite',
    version='1.0',
    py_modules=['calvite'],
    install_requires=[
        'Click',
        'datetime',
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib',
    ],
    entry_points='''
        [console_scripts]
        cal=calvite:cli
    '''

)
