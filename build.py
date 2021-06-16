# echo 'layout python3' > .envrc
# direnv allow
# pip install ninja

import glob
from pathlib import Path

files = glob.glob("org/**/*.org", recursive=True)

with open('build.ninja', 'w') as ninja_file:
    ninja_file.write("""
rule org2md
  command = emacs --batch -l publish.el --eval \"(my--org-roam-publish \\"$in\\")"
  description = org2md $in
""")

    i = 1
    for f in files:
        i += 1
        print(i)
        path = Path(f)
        # relative_path = path.relative_to(*path.parts[:1])
        # output_file = f"content/notes/{relative_path.with_suffix('.md').as_posix()}"
        output_file = f"content/notes/{path.with_suffix('.md').name}"
        print(output_file)
        ninja_file.write(f"""
build {output_file}: org2md {path}
""")

import subprocess
subprocess.call(["ninja"])
