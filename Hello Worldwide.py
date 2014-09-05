print ('Hello')
print ('What is your name')

Name = raw_input()
print "###"
print Name

print ('Hello ' + Name + ', Hello World')
print ('I can say that in English, Dutch, French, German and Spanish.')
print ('What language would you like me to speak in')

Dutch = ('hallo' + Name + ' hallo wereld')
English = ('Hello ' + Name + ', Hello World')
French = ('bonjour ' + Name + ' bonjour tout le monde')
German = ('hallo ' + Name + ' hallo Welt')
Spanish = ('hola ' + Name + ' hola mundo')

chosen_lang = raw_input().lower()
print chosen_lang

if chosen_lang == 'spanish':
    print Spanish
if chosen_lang == 'german':
    print German
if chosen_lang == 'french':
    print French
if chosen_lang == 'dutch':
    print Dutch
if chosen_lang == 'english':
    print English
        
