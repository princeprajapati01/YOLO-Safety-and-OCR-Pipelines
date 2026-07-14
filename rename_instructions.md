# Suggested folder renames (safe `git mv` commands)

These are suggested, non-destructive renames to make the repository clearer before pushing. Run the commands below from the repository root.

Suggested mapping:

- `adv_model` -> `models/adv_model`
- `basic_01` -> `experiments/basic_01`
- `construction_main` -> `apps/construction_main`
- `helmetdetection` -> `projects/helmet_detection`
- `opencv_code` -> `tools/opencv_code`
- `datasets` -> `datasets/raw`
- `train` -> `datasets/train`
- `valid` -> `datasets/valid`

Run these commands (example):

```
git mv adv_model models/adv_model
git mv basic_01 experiments/basic_01
git mv construction_main apps/construction_main
git mv helmetdetection projects/helmet_detection
git mv opencv_code tools/opencv_code
git mv datasets datasets/raw
git mv train datasets/train
git mv valid datasets/valid
```

If any target directory doesn't exist, create it first with `mkdir <dir>` or use `git mv -k` behaviour by creating parent directories.

After renaming, run:

```
git add -A
git commit -m "Rename folders for clarity"
git push
```
