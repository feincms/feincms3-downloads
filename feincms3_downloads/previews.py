import io
import subprocess
import tempfile


def preview_as_jpeg(path):
    with tempfile.TemporaryDirectory() as directory:
        preview = "%s/preview.jpg" % directory
        if path.lower().endswith(".pdf"):
            cmd = [
                "pdftocairo",
                path,
                "-jpeg",
                "-singlefile",
                "-scale-to-x",
                "300",
                "-scale-to-y",
                "-1",
                preview.replace(".jpg", ""),
            ]
        else:
            cmd = [
                "convert",
                "-resize",
                "300x300>",
                "-quality",
                "90",
                "%s[0]" % path,
                preview,
            ]

        # print(cmd)
        ret = subprocess.call(cmd, env={"PATH": "/usr/local/bin:/usr/bin:/bin"})

        if ret == 0:
            with io.open(preview, "rb") as f:
                return f.read()
