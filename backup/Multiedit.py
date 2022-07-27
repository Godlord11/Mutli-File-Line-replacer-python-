import os
n=0

# number of the amount of lines to be replaced #
for n in range (32):             

    texttofind = ['# this is where your lines will be placed',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '']


    texttoreplace = ['# this is where your replace line will be placed',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '',
                     '']
    
    sourcepath = os.listdir('InputFiles/')
    
    for file in sourcepath:
        inputfile = 'InputFiles/'+ file
        print('Conversation is ongoing for:' +inputfile)
        
        with open(inputfile,'r') as inputfile:
            filedata = inputfile.read()
            freq = 0
            freq = filedata.count(texttofind[n])
        
        destinationpath = 'InputFiles/' + file 
        filedata = filedata.replace(texttofind[n],texttoreplace[n])
        with open(destinationpath, 'w') as file: 
            file.write(filedata)
            print ('Total %d Record Replaces' %freq)
            n = n+1