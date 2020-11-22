.. _my-reference-label:

YAML Format (input)
+++++++++++++++++++
Each question is provided in `yaml` format. The format is somewhat unforgiving as spacings and alignments need to be correct for the file to be readable. Below is an example of a question using this format. Each line will be described in details.

Question example
----------------
.. code-block:: yaml
  :linenos:

     - Type: MC
       Text: >-
        In the screencast we derived an expression for the Fermi-Dirac distribution 
        using the grand canonical ensemble. What is the grand canonical ensemble?
       Size: Auto
       Points: 2
       Answers:
	- Choice:  >-
            The ensemble of systems with fixed energy and entropy.
          Validity: incorrect
	- Choice: >-
            The ensemble of systems with fixed energy and chemical potential.
          Validity: incorrect
	- Choice: 'The ensemble of systems with fixed temperature and chemical potential.'
          Validity: correct
	Skip: 'no'
	Note: question regarding lecture 29 

Anatomy of a question
---------------------
	
We will now review each line. Basically, all names that are followed by ":" is a key in a dictionary. If you wish to use a ":" in your questions or answers, you need to use quotation marks (or the :code:`>-` sign -- it is usually used for text with multiple lines).

1. New question starts with the type. 

.. code-block:: yaml

   - Type: MC		

Each new question starts with a :code:`- Type:` keyword. The options are: :code:`MC` (Multiple Choice), :code:`MA` (Multiple Answers),...

2. Description of the question itself.

.. code-block:: yaml

   - Text: 'This is my question'


or

.. code-block:: yaml

   - Text: >-
      This is a multiline question with various parts in it.
      Try it if you want to. 


.. Tip:: The advantage of this approach is that you can use LaTeX commands in both text and math modes in all the text used in the *yaml* file.

3. For multiple-choice questions, you then have the list of possible answers: 

.. code-block:: yaml

   Answers:
	- Choice:  >-
            The ensemble of systems with fixed energy and entropy.
          Validity: incorrect	 
	 
Each Choice can be entered in a single-line or multiline format. There is a second keyword called :code:`Validity` (case sensitive) to assign an `incorrect` or `correct` attribute to the choice. Note that you only need to provide the information for a *correct* asnwer as the script will assign an *incorrect* attribute by default.

- Note 1: You can list as many *Choice* lines as you need.
- Note 2: For some types of questions, only one answer can have the :code:`Validity: correct` attribute.

4. You can skip the question from the file without deleting it by using: :code:`Skip: 'no'` (this is an optional keyword)

5. To keep things tidy, you can add a note for each question, using the :code:`Note:` keyword. 

.. note:: The easiest way to create a question is to use an existing one as a template!

.. hint:: A good habit is to check your `yaml` file using a free online tool such as those provided by onlineyamltools.com (see, here: https://onlineyamltools.com/validate-yaml). After a while you won't make a mistake anymore but early on, this could be frustrating.

