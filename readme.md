
## CS101-animation-to-gifs

This project helps you to convert KAIST CS101 animation scripts into gif files.

### How does this work

This application overrides `time.sleep` function and save frame images while
animation script sleeps, and convert frames into GIF file afterwards.

To do this, a customized `cs1graphics` library is used with animation scripts
that has additional code lines injected before the original code
and after the original code.

### How to use

Prepare Python 3.5 or 3.6 installed on your environment and
make sure to install **Pillow**, **imageio** with pip and let their external dependencies all met.

Make `cs101-animation-to-gif/sources` directory and put all
`*.py` animation scripts with the student ids included in the filename.
For example:

`cs101-animation-to-gif/sources/20134495_Jeongmin_Byun,20155513_Jeongmin_Byun.py`

When all scripts you want to convert are prepared in `cs101-animation-to-gif/sources`, run `$ python3 convert_sources.py`.

This will convert all scripts into gif files as `cs101-animation-to-gif/gifs/src_{student_ids_separated_by_underscore}.py.gif`.

Be aware that this application will not be able to convert
erroneous animation scripts and scripts that does not depend on `timer.sleep()`
to draw animations.
