#!/bin/python3

"""
Python

Input:

Output:


"""

import clr

if __name__ == '__main__':

    clr.AddReference("System.Windows.Forms")
    from System.Windows.Forms import MessageBox
    MessageBox.Show("Hello World")
