.. _download-label:

Download
++++++++

*yam2lms* is just a python script. It can be obtained below: 

.. code-block:: python

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    Created on Sat Aug 29 17:49:38 2020
    
    @author: vmeunier
    """
    #38add: scp -r Questions_THERMO_quiz14 meuniv@rcs.rpi.edu:~/public_html/Images/TSM_F20/.
    
    import yaml
    from textblob import TextBlob
    from distutils.util import strtobool
    from spellchecker import SpellChecker
    
    with open("config.yaml") as conf: 
        configuration = yaml.load(conf, Loader=yaml.FullLoader)
        
    yamlfile=configuration['yamlfile']
    spellcheck=configuration['spellcheck']
    create_LMS=configuration['createLMS']  
    create_LMS_text=configuration['createLMS_text']    
    base=configuration['base']
    dir=configuration['dir']
    title1=configuration['title1']
    title2=configuration['title2']
    solutions=configuration['solutionKey']
    
    print(yamlfile)
    
    with open(yamlfile) as f: 
        myset = yaml.load(f, Loader=yaml.FullLoader)
    
    print(myset)
    
    class Question:  
        def __init__(self, Type, Text, Size, Choice, Valid):  
            self.Type = Type
            self.Text = Text 
            self.Size = 'Auto'
            self.Points = '0' 
            self.Skip = 'False' 
            self.TextString = Text 
            self.Choice = []
            self.ChoiceString = []
            self.Valid = []
            self.ValidString = []
                    
        def out(self):
            string="%s\t%s" % (self.Type,self.Text)
            for i in range(len(self.Choice)):
                string+='\t%s \t%s' %  (self.Choice[i], self.Valid[i])
            string+='\n' 
            return string
        
        def outpng(self):
            string="%s\t%s" % (self.Type,self.TextString)
            for i in range(len(self.ChoiceString)):
                string+='\t%s \t%s' %  (self.ChoiceString[i], self.ValidString[i])
            string+='\n' 
            return string        
    
    #here we want to translate input into the question class and populate it
    MyQuestions=[]
    l=len(myset)
    print(l)
    for q, question in enumerate(myset):
        ThisQuestion=Question('MC','','','','')
        if 'Type' in question.keys():
            ThisQuestion=Question(question['Type'],'','','','')
        ThisQuestion.Text=question['Text']
        if 'Size' in question.keys():
            ThisQuestion.Size=question['Size']
        else: 
            ThisQuestion.Size='Auto' 
        nanswers=len(question['Answers']) 
        for i in range(nanswers):
            ThisQuestion.Choice.append(question['Answers'][i]['Choice'])
            if 'Validity' in question['Answers'][i].keys():
                ThisQuestion.Valid.append(question['Answers'][i]['Validity'])
            else:
                ThisQuestion.Valid.append('incorrect')
        if 'Skip' in question.keys():        
            ThisQuestion.Skip=strtobool(question['Skip'])
        else: 
            ThisQuestion.Skip=strtobool('no')
    
        if not ThisQuestion.Skip: 
            MyQuestions.append(ThisQuestion)
    
        
        
    #spell checking
      
    def correctstring(string):
        splits=string.split()
        for i, word in enumerate(splits):
            if "$" not in word and "\\" not in word:
                #print(word)
                wordy=TextBlob(word)
                if wordy != wordy.correct():
                    splits[i]="\\sout{\\textcolor{red}{" + word + "}} \\textcolor{blue}{" + str(wordy.correct())+"}"
        newstring=' '.join(splits)
        return newstring
    
      
    def correctstring2(string):
        spell=SpellChecker()
        splits=string.split()
        misspelled=spell.unknown(splits)
        
        for i, word in enumerate(misspelled):
        # Get the one `most likely` answer
            splits[i]=spell.correction(word)
    
        newstring=' '.join(splits)
        return newstring
                    
        
    import os
    os.environ["PATH"] += os.pathsep + '/Library/TeX/texbin/'
    os.environ["PATH"] += os.pathsep +'/usr/local/bin/'
    def latexsize(string,filename):    
        size='auto'
        with open("temporary.tex","w") as myfile:
           myfile.write("\\documentclass[preview]{standalone}\n")
           myfile.write("\\usepackage[fleqn]{amsmath}\n")
           myfile.write("\\usepackage{physics}\n")
           myfile.write("\\usepackage[T1]{fontenc}")
           myfile.write("\\newcommand{\\dbar}{\\text{\\dj}}")
           myfile.write("\\DeclareUnicodeCharacter{2212}{-}")
           myfile.write("\\begin{document}\n") 
           myfile.write("\\setlength{\\mathindent}{3pt}\n")
           #myfile.write("\\setlength{\\abovedisplayskip}{3pt}\n")
           myfile.write("\\newcommand{\\makenonemptybox}[2]{%\n")
           myfile.write("\\par\\nobreak\\vspace{\\ht\\strutbox}\\noindent\n")
        #FIXME: make this part of option
        #put back if you want a box around the box
        #   myfile.write("\\fbox{%\n")
           myfile.write("\\parbox[c][\\dimexpr#1-2\\fboxsep][c]{\\dimexpr\\linewidth-6\\fboxsep}{\n")
           myfile.write("\\hrule width \\hsize height 0pt\n")
           myfile.write("  #2\n")
        #put back if you want a box around the box
        #   myfile.write(" }%\n")
           myfile.write("}%\n")
           myfile.write("\\par\\vspace{\\ht\\strutbox}\n")
           myfile.write("}\n")
           myfile.write("\\makeatother\n")
           string=string.replace("$$","\\begin{equation*}",1)
           string=string.replace("$$","\\end{equation*}",1)
           size2=size.strip()
        
           if size2.lower()=="auto": #automatic height is size is negative
               #print(string)
               myfile.write("\\parbox[c]{\\textwidth}{\\begin{flushleft}\n%s\n\\end{flushleft}} \n" % string)
           else: #fixed height if size is provided (Auto is default)
               myfile.write("\\makenonemptybox{%s}{%s} \n" % (size, string))
        
           myfile.write("\\end{document}\n")
           myfile.close()
           
           x = os.system("pdflatex temporary.tex > latex.log 2>&1 && gs -sDEVICE=pnggray -sBATCH -sOutputFile=%s -dNOPAUSE -r1200 temporary.pdf > latex.log 2>&1" % filename)
           
           if x !=0:
               print ('Exit code not 0, check result!')
           else:
               #os.system('open %s' % filename)
               os.system('rm temporary.tex')
    
    
    def latexquestionnaire(Questions,solutions,yamlfile):
        if solutions:
            answers='answers'
            filepdf=yamlfile.rsplit(".",1)[0]+"_solutions.pdf" 
            filelatex=filepdf.rsplit(".",1)[0]+".tex"
        else:
            answers=''
            filepdf=yamlfile.rsplit(".",1)[0]+".pdf"
            filelatex=filepdf.rsplit(".",1)[0]+".tex"
    
        with open(filelatex,"w") as flatex:
            flatex.write("\\documentclass[%s]{exam}\n" % answers)
            flatex.write("\\usepackage{physics}\n")
            flatex.write("\\usepackage[T1]{fontenc}\n")
            flatex.write("\\usepackage[normalem]{ulem}\n")
            #below is special macro for Thermo! 
            flatex.write("\\newcommand{\\dbar}{\\text{\\dj}}\n")
            flatex.write("\\usepackage[margin=.75in]{geometry}\n")
            flatex.write("\\usepackage{lastpage}\n")
            flatex.write("\\usepackage{color}\n")
            flatex.write("\\usepackage[T1]{fontenc}\n")
            flatex.write("\\DeclareUnicodeCharacter{2212}{-}")
            flatex.write("\\firstpageheader{% left\n")
            flatex.write("%s\\\\\n" % title1)
            flatex.write("%s\n" % title2)
            flatex.write("}{% center\n")
            flatex.write("}{% right\n")
            flatex.write("\ifprintanswers \\textbf{Answer Key}\n")
            flatex.write("   	\\fi}\n") 
            #flatex.write("\\runningheader{}{}{}\n")
            #flatex.write("\\firstpagefooter{}{\\thepage/\pageref{LastPage}}{}\n")
            #flatex.write("\\runningfooter{}{\\thepage/\pageref{LastPage}}{}\n")           
            #flatex.write("\\frenchspacing\n")
            flatex.write("\\unframedsolutions\n")
            flatex.write("\\SolutionEmphasis{\\sffamily}\n")
            flatex.write("\\renewcommand{\\solutiontitle}{Answer:~}\n")
            flatex.write("\\makeatother\n")
            flatex.write("\\extraheadheight{.35in}\n")
            flatex.write("\\extrafootheight{.15in}\n")
            flatex.write("\\setlength{\\marginparwidth}{1.5in}\n")
            flatex.write("\\nopointsinmargin\n")
            flatex.write("\\pointformat{}\n")
            flatex.write("\\CorrectChoiceEmphasis{\\color{red}\\bfseries}\n")
    
            flatex.write("\\begin{document}\n")
            flatex.write("\\begin{questions}\n")
            for q, question in enumerate(Questions):
                flatex.write("\\question %s\n" % question.Text)  
                flatex.write("\\begin{choices}\n")
                for i in range(len(question.Choice)):
                    if(solutions and question.Valid[i].lower() == "correct"):
                        flatex.write("\\CorrectChoice %s\n" % question.Choice[i])
                    else:
                        flatex.write("\\choice %s\n" % question.Choice[i])
                flatex.write("\\end{choices}\n")
                flatex.write("\n")
            flatex.write("\\end{questions}\n")   
            flatex.write("\\end{document}\n")
            flatex.close()
        x = os.system("/Library/TeX/texbin/pdflatex %s > latex.log2 2>&1" % filelatex)
        #need to run twice to get total number of points correctly added
        x = os.system("/Library/TeX/texbin/pdflatex %s > latex.log2 2>&1" % filelatex)
        if x !=0:
            print ('Exit code not 0, check result! %s ' % filepdf)
        os.system("open %s" % filepdf)            
    
    if spellcheck:
        #spell checking and provide latex file with proposed corrections
        #we do not touch the original questions
        #the users must make the changes themselves
        import copy
        MyNewQuestions=copy.deepcopy(MyQuestions)
    
        for question in MyNewQuestions:
            question.Text=correctstring(question.Text)
            for i, choice in enumerate(question.Choice):
                question.Choice[i]=correctstring(question.Choice[i])
    
        filepdf=yamlfile.rsplit(".",1)[0]+"SPELLCHECKED.pdf"
        latexquestionnaire(MyNewQuestions,False,filepdf)
    
    #now the original file         
    
    
    
    latexquestionnaire(MyQuestions,solutions,yamlfile)
    
    if create_LMS_text: 
     #This is for un-latexized version of the questions
        filename=yamlfile.rsplit(".",1)[0]+"_LMS_text.txt"
        f = open(filename, "w")
        for q in MyQuestions: #run over all questions
            f.write(q.out().replace("$","$$"))
        f.close()
    
    #ID = "THERMO_"+yamlfile.rsplit(".",1)[0] #we remove suffix but only last one
    ID = dir+"_"+yamlfile.rsplit(".",1)[0] #we remove suffix but only last one
    if create_LMS:
        myfolder='Questions_%s' % ID
        scp_string='scp -r '+myfolder+'  meuniv@rcs.rpi.edu:~/public_html/Images/TSM_F20/.'
    
        print("PNG files will be stored at %s " % myfolder)
        if not os.path.exists(myfolder):
            print("Directory does not exist, creating it\n")
            os.makedirs(myfolder)         
        else:
            print("Directory already exists. Files will be replaced.\n")    
    
        #this is for latexized version of the questions
        filename=yamlfile.rsplit(".",1)[0]+"_LMS_png.txt"
    
        fpng = open(filename, "w")
        j=0
        for q in MyQuestions: #run over all questions
            p=j+1
        # one directory per question
            myfolder2=myfolder+"/Q%s" % j
            if not os.path.exists(myfolder2):
                os.makedirs(myfolder2)         
        
            print("\t Question type: %s" % q.Type)
            filename=myfolder2+"/Q%s.png" % j
            latexsize(q.Text,filename)
            print(q.Text)
            filename=base+filename
            q.TextString="<p><img src=\"%s\" height=\"33\" /></p>" % filename
        
        
            for i in range(len(q.Choice)):
                filename=myfolder2+"/Q%s_%s.png" % (j, i)
                latexsize(q.Choice[i],filename)
                filename=base+filename
                q.ChoiceString.append("<p><img src=\"%s\" height=\"33\" /></p>" % filename)
        
                if q.Type.lower() == "mat" :
                    filename=myfolder2+"/S%s.png" % i
                    latexsize(q.Valid[i],filename)
                    filename=base+filename
                    q.ValidString.append("<p><img src=\"%s\" height=\"33\" /></p>" % filename)
                else : 
                    q.ValidString.append(q.Valid[i])
        
            
            fpng.write(q.outpng())
            j=j+1
    
        fpng.close()
        print("To copy for LMS use, executive: %s" % scp_string)
        
        
        
        
