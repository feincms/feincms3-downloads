import io
import subprocess
import tempfile


def preview_as_jpeg(path, *, resize="300x300>"):
    with tempfile.TemporaryDirectory() as directory:
        cmd = ["convert", "-resize", resize, "-quality", "90"]

        if path.lower().endswith(".pdf"):
            cmd.extend(["-background", "white", "-alpha", "remove"])

        cmd.extend(["%s[0]" % path, "%s/preview.jpg" % directory])

        # print(cmd)
        ret = subprocess.call(cmd, env={"PATH": "/usr/local/bin:/usr/bin:/bin"})

        if ret == 0:
            with io.open("%s/preview.jpg" % directory, "rb") as f:
                return f.read()
