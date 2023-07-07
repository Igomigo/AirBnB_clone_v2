#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, task


@task
def do_pack():
    """Archives the static files."""
    if not os.path.exists("versions"):
        local("mkdir versions")

    date = datetime.now()
    output = "versions/web_static_{}.tgz".format(date.strftime(
        "%Y%m%d%H%M%S"))

    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.path.getsize(output)
        print("web_static packed: {} -> {}Bytes".format(output, size))

    except OSError:
        output = None
        print("An error occurred")

    return output
