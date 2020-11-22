.. _config-label:

Basic usage and configuration file
++++++++++++++++++++++++++++++++++

The process is simply to run the python script (see :ref:`download-label`) in a directory where the :code:`config.yaml` file described below is located. A *question* file must also be findable (see :code:`yamlfile:` keyword below). 

Configuration file
------------------

All the necessary configuration information is provided in the :code:`config.yaml` input file. The file reads as:

.. code-block:: yaml

   yamlfile: quiz20.yaml
   spellcheck: no
   createLMS: yes
   createLMS_text: no
   base: "http://homepages.rpi.edu/~meuniv/Images/TSM_F20/"
   dir: "THERMO"
   title1: 'PHYS {4420}: Thermodynamics and Statistical Mechanics (Quiz 20)'
   title2: "Dr. Vincent Meunier, Fall 2020"
   solutionKey: no

The various keywords (ending with a :code:`:`) are mostly self-explanatory.

1. :code:`yamlfile` provides the actual file with the list of questions (see here: :ref:`my-reference-label`)

2. :code:`spellcheck` is a *yes/no* input (more information can be found here: :ref:`spellcheck-label`)

3. :code:`createLMS` and :code:`createLMS_text` are *yes/no* answers (see here: :ref:`lms-label`)

4. :code:`base` is only used if the  :code:`createLMS: yes` is used. It is also described in :ref:`lms-label`.

5. :code:`dir` is only used if the  :code:`createLMS: yes` is used. It is also described in :ref:`lms-label`.

6. :code:`title1` and :code:`title2` are used to assemble the PDF files (both the raw exam and the version with answer keys when requested)

7. :code:`solutionKey` is a *yes/no* input. This provides the answer Key in a PDF file with highlighted answers (see here :ref:`pdf-label`)


.. Note:: This configuration file was used to create the examples shown in :ref:`example`. 


