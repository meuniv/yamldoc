General purpose
+++++++++++++++
We are often faced with creating quizzes, assigments, and online tests using tools such as *canvas* or even simply writing LaTeX files for distribution. Platforms such as *blackboard* make it possible to realize that objective but their format is *unforgiving* and does not allow for advanced formatting (including the insertion of math symbols). At the same time, we wish to keep those questions in a raw form so that they can be archived, edited, and reused. Here, I introduce the use of a standard *yaml* file for this purpose. The goal of *yaml2lms*  is to convert a `yaml` file into a file usable for multiple-choice questions in LMS. The code also creates LaTeX and PDF files as needed. 

In addition to creating neat files, this approach is a good way to archive questions in a flexible format and it also provides a spellchecking utility. 

.. Warning:: *yaml2lms* is a hack. No question about it. It was written as a utility that has saved me a lot of time and headache as a *certain* pandemic forced online teaching. It is not an example of best practice in coding but it works. It really does (I think).
	       
Functionalities
---------------

1) Creation of files needed for integration with LMS or Canvas, including math symbols. 
2) Creation of latex files using the exam class.
3) Creation of latex files with answer keys.
4) Spellchecking.

Installation
------------
There is no installation needed as this is a simple Python script. It can be downloaded from :ref:`download-label`.

Just make sure to have:

1. A working LaTeX environment in place
2. Python installed

.. Note:: If you wish to use specific LaTeX packages in your mathematical formulas, you will need to edit the python script directly. There is work in progress to make this process simpler. 

.. Hint:: Feel free to contact `me`_ by email for any question!

.. _me: vinmeunier@gmail.com
