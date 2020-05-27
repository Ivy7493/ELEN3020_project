# ELEN3020_project
This program is to be used to for the management of a Biobank's samples.

## Installations
### tkinter
Run the following line in the Linux terminal to install tkinter using [apt](http://manpages.ubuntu.com/manpages/xenial/man8/apt.8.html?_ga=2.263955596.1483418505.1590566923-1057169257.1590566923):
```bash
sudo apt-get install python-tk
```

### tkCalendar
Run the following lines in the Linux terminal to install tkCalendar with [apt](http://manpages.ubuntu.com/manpages/xenial/man8/apt.8.html?_ga=2.263955596.1483418505.1590566923-1057169257.1590566923):
```bash
$sudo add-apt-repository ppa:j-4321-i/ppa
$sudo apt-get update
$sudo apt-get install python3-tkcalendar
```

Or use the package manager [pip](https://pip.pypa.io/en/stable/) to install tkCalendar:
```bash
$pip install tkcalendar
```

### FPDF
Use the package manager [pip3](http://manpages.ubuntu.com/manpages/disco/en/man1/pip.1.html?_ga=2.230319260.1483418505.1590566923-1057169257.1590566923) to install FPDF by running the following lines in the Linux terminal:
```bash
pip3 install --upgrade setuptools
pip3 install fpdf
```

## Further Setup
### Cron
Run the following line of code in the Linux terminal to open Cron in edit mode:
```bash
crontab -e
```
Enter the following text. Please replace the example path with the appropriate paths to the program's root folder. Save and close the terminal window.
```bash
0 0 1 * * cd /path/to/script/folder && /usr/bin/python3 /path/to/script/folder/script.py  >> /path/to/script/folder/Logs/BillingLog.txt
```

## Starting the Program
Open a Linux terminal directly in the root folder of the program. In this window, run the following line to start the program:
```bash
python3 program.py
```

The default login details are: 
Username | Password
--------|--------
admin|admin
