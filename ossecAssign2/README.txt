This program only works on Linux systems.

About this package:

This package includes a README.txt, the password cracking script, and a 
small dictionary.

The dictionary contains several words that the script will encrypt and
compare to the password hash of the chosen user.

Because this script accesses the passwd and shadow files, you must have root
access to successfully run this program.

Instructions:

1. Open the Linux terminal
2. Type "sudo su" + enter
3. If you have a password set for the superuser, type it when the terminal
   prompts you to
4. Type "python ossecAssign2.py" + enter
5. You will see "Enter the username: ", please enter the chosen username
6. If the username exists, the script will move on to finding the password in
   the shadow file
7. If the username does not exit, a message will alert you and the script will quit
8. If the password is blank, a message will alert you and the script will quit
9. If the password is a valid hash, it will be compared against a hash of each 
   entry in the dictionary provided

Good luck and happy password cracking!
