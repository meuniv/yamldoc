General purpose
+++++++++++++++
The purpose of this tool is to convert a `yaml` file into a file usable for 
multiple-choice questions in LMS. The code also creates  :math:`\textrm{\LaTeX}` and PDF files as needed. 

In addition to creating neat files, this approach is a good way to archive questions in a flexible format.

.. Warning:: *yaml2lms* is a hack. No question about it. It was written as a utility that has saved me a lot of time and headache as a *certain* pandemic forced online teaching. It is not an example of best practice in coding but it works. It really does (I think).
	       
Functionalities
---------------

1) Creation of files needed for integration with LMS or Canvas, including math symbols. 
2) Creation of latex files using the exam class.
3) Creation of latex files with answer keys.
4) Spellchecking.

Installation
------------
There is no installation needed as this is a simply Python script.

Just make sure to have:

1. A working  :math:`\textrm{\LaTeX}` environment in place
2. Python installed

.. Note:: If you wish to use specific LaTeX packages in your mathematical formulas, you will need to edit the python script directly. There is work in progress to make this process simpler. 

