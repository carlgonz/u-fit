from distutils.core import setup

setup(
    name='u-fit',
    version='0.0.3',
    url='https://github.com/carlgonz/u-fit',
    license='MIT',
    author='Carlos Gonzalez',
    author_email='cgonzalez@alges.cl',
    description='A software fot automated curve fitting',

    packages=['src/python/forms', 'src/python/modules', 'src/python', ''],
    scripts=['u-fit.py'],
    install_requires=["numpy", "scipy", "pygal"],
    data_files=[('src/css', ['src/css/base-new.css']),
                ('src/js', ['src/js/pygal-tooltips.js', 'src/js/svg.jquery.js'])]
)
