from distutils.core import setup

setup(
    name = "thanks_virgil",
    package_dir = {'thanks_virgil': 'lib/thanks_virgil'},
    packages = ["thanks_virgil"],
    install_requires = ["ansible",
                        "jinja2",
                        "linode-python",
                        "pycurl",
                        "Flask",
                        "Flask-Script"]
    version = "0.0.1",
    description = "srcds deployment tool",
    author = "Jon Chen",
    author_email = "dabestmayne@burrito.sh",
    url = "https://github.com/fly/thanks_virgil",
    download_url = "https://github.com/fly/thanks_virgil/archive/0.0.1.tar.gz",
    keywords = ["srcds", "deployment"],
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Environment :: Other Environment",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Systems Administration",
        ],
    long_description = """\
srcds Game Server Deployment Tool
---------------------------------

Integration with:
  - Ansible

Eventually will be a Flask web application.

This version requires Python 2.7.6 or later, due to Ansible requirement.
"""
)
