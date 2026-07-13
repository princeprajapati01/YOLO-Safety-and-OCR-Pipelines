Open CV Model Workspace

This repository contains experiments, trained models, datasets, and helper code for computer vision projects (YOLO/OpenCV).

Purpose of this change:

- Add brief READMEs to clarify folder intent.
- Provide a safe mapping and a PowerShell script to rename folders using `git mv` before pushing.

Workflow:

1. Inspect `rename_instructions.md` for the proposed mapping.
2. (Optional) Run `.
ename_folders.ps1` from PowerShell to apply `git mv` commands.
3. Commit and push: `git add -A && git commit -m "Organize repo and add READMEs" && git push`

Files added:

- [rename_instructions.md](rename_instructions.md)
- [rename_folders.ps1](rename_folders.ps1)
