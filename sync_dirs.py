"""This module defines various groups of directories for backing up
with unison and rsync."""
# directories that should be included with pretty much every
# backup
quick_all = ['scripts', \
             '.profile', \
             '.inputrc', \
             '.gitconfig', \
             '.gitexcludes', \
             '.gitignore', \
             '.emacs', \
             'elisp', \
             'siue/classes/Spring_2016', \
             'siue/admin/grad_committee', \
             'siue/Research/papers/ACC/2016_zumo_RPi_Arduino', \
             'git/research', \
             'git/krauss_misc', \
             'git/olliei2c', \
             'git/teaching', \
             'git/olliespi', \
             ]

# add specific Research/work folders latter

weekly_all = ['siue/Research/presentations/ACC/2016_zumo_RPi_Arduino', \
              'siue/Research/students/vahid', \
              'siue/Research/work', \
              'git/report_generation', \
              'git/restutils', \
              'git/rpi_arduino_communication', \
              'git/rst2beamer', \
              'git/wxpython_guis', \
              'git/pygtk_guis', \
              'git/pygtk_utils', \
              'git/zumo_serial', \
              'git/raspberry_pi_learn', \
              ]