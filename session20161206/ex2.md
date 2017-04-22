virtualenv on cloud9

lcarbonaro:~/workspace (master) $ virtualenv
bash: virtualenv: command not found

lcarbonaro:~/workspace (master) $ sudo apt-get install python-virtualenv
E: Package 'python-virtualenv' has no installation candidate
lcarbonaro:~/workspace (master) $ sudo apt-get update

lcarbonaro:~/workspace (master) $ sudo apt-get install python-virtualenv

lcarbonaro:~/workspace (master) $ virtualenv
You must provide a DEST_DIR
Usage: virtualenv [OPTIONS] DEST_DIR

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v, --verbose         Increase verbosity.


---------------------------------------------

weather api