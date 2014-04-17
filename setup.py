from distutils.core import setup

setup(
    name='u-regression',
    version='0.0.2',
    url='https://github.com/carlgonz/u-regression',
    license='MIT',
    author='Carlos Gonzalez',
    author_email='cgonzalez@alges.cl',
    description='A software fot automated curve fitting',

    packages=['src/python/forms', 'src/python/modules', 'src/python', ''],
    scripts=['u-regression.py'],
    install_requires=["numpy", "scipy", "pygal"],
    data_files=[('src/css', ['src/css/base-new.css']),
                ('src/js', ['src/js/pygal-tooltips.js', 'src/js/svg.jquery.js'])]
)
