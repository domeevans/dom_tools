import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dom_tools',
    version='0.0.5',
    author='Dominic Evans',
    author_email='dominic.evans@decathlon.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/domeevans/dom_tools',
    project_urls = {
        "Bug Tracker": "https://github.com/domeevans/dom_tools/issues"
    },
    license='MIT',
    packages=['dom_tools'],
    install_requires=['requests', 'pandas'],
)
