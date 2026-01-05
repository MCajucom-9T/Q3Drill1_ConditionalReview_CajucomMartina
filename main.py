from pyscript import display, document

subjects = ['Math:', 'English:', 'Science:', 'Filipino:', 'ICT:', 'PE:']

display(f'{subjects[0]}', target='mlabel')
display(f'{subjects[1]}', target='elabel')
display(f'{subjects[2]}', target='slabel')
display(f'{subjects[3]}', target='flabel')
display(f'{subjects[4]}', target='ilabel')
display(f'{subjects[5]}', target='plabel')

def generating_grade(e):
    units = (5,3,2,1)
    z,y,x,w = units
    first = document.getElementById('fname').value # collecting value from an input field
    last = document.getElementById('lname').value 
    math = int(document.getElementById('mvalue').value) * z
    english = int(document.getElementById('evalue').value) * z
    science = int(document.getElementById('svalue').value) * z
    filipino = int(document.getElementById('fvalue').value) * y
    ict = int(document.getElementById('ivalue').value) * x
    pe = int(document.getElementById('pvalue').value) * w
    inmath = int(document.getElementById('mvalue').value) 
    inenglish = int(document.getElementById('evalue').value) 
    inscience = int(document.getElementById('svalue').value) 
    infilipino = int(document.getElementById('fvalue').value) 
    inict = int(document.getElementById('ivalue').value) 
    inpe = int(document.getElementById('pvalue').value) 
    GWA = round((math + english + science + filipino + ict + pe)/21, 2)

    #displays student info
    display(f'{GWA}', target='GWA')
    display(f'{first} {last}', target='name')
    display(f'{subjects[0]} {inmath}', target='math')
    display(f'{subjects[1]} {inenglish}', target='eng')
    display(f'{subjects[2]} {inscience}', target='sci')
    display(f'{subjects[3]} {infilipino}', target='fil')
    display(f'{subjects[4]} {inict}', target='ict')
    display(f'{subjects[5]} {inpe}', target='pe')

    if GWA > 74:
        display(f'You have passsed', target='remarks')
    else:
        display(f'You have failed', target='remarks')