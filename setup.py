from distutils.core import setup

setup(
    name='u_fit',
    version='0.0.3',
    url='https://github.com/carlgonz/u_fit',
    license='MIT',
    author='Carlos Gonzalez',
    author_email='cgonzalez@alges.cl',
    description='A software fot automated curve fitting',

    packages=['u_fit', 'u_fit.modules', 'u_fit.forms'],
    package_dir={'u_fit': 'src/python/u_fit'},
    package_data={'u_fit': ['data_css/*.css', 'data_js/*.js']},

    scripts=['u-fit.py'],
    include_package_data=True,
    install_requires=["numpy", "scipy", "pygal"]
)
