.. _pdf-label:

Portable Data File creation
+++++++++++++++++++++++++++

By default, *yaml2lms* always creates a PDF file, using latex processing and the exam_ class. The output file name (**<prefix>.pdf**) is built based on the *yaml* file name provided using :code:`yamlfile: <prefix>.yaml` in *config.yaml*.

The document will have a two-line title, provided by the tags :code:`title1` and :code:`title2` in the *config.yaml* file.

An example of PDF file output is shown in :ref:`example`.

Two additional PDF files can be created if requested in the *config.yaml* files as described below.

.. Hint:: During PDF file creation, a **<prefix>.tex** is also created. If the PDF file fails to compile (because of an issue with your latex input), you can directly refer to the latex source. You can also fine-tune that file as necessary.
	  
Answer Key PDF file
-------------------

If :code:`solutionKey: yes` is specified, in addition to the questionnaire itself, a file, named **<prefix>_solutions.pdf** is created where the *correct* asnwers are highlighted. (See  :ref:`example` for an example).

Spellchecked PDF file
---------------------

If :code:`spellcheck: yes` is specified, *yaml2.lms* performs a rudimentary spell checking of the input. This feature is described in details at :ref:`spellcheck-label`.


.. Note:: It is recommended to carefully check the PDF files before starting the process of creating LMS files. The :code:`createLMS: yes` option can take a few minutes or so to process, depending on the number of questions. And it is best to perform this once you have checked the spelling and the correctness of the answer keys. Note, also, that the spellchecking is time consuming and once you are done spellchecking, it is best to turn that option off. 


.. _exam: http://www-math.mit.edu/~psh/exam/examdoc.pdf
