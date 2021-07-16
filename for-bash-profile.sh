# If you have the .py file somewhere on your computer, you can create an alias
# in your .bash_profile file and play deal or no deal on your terminal
# without having to type in the full path of the .py file each time.

# Either of these will work

alias deal-or-no-deal=py { pathToPythonFile }/deal-or-no-deal.py

function deal-or-no-deal() {
    py { pathToPythonFile }/deal-or-no-deal.py
}
