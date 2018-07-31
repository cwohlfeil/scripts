import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.search('My number is 415-555-4242'))

phoneNumRegexGroups = re.compile(r'\(\d\d\d\) (\d\d\d-\d\d\d\d)')
print(phoneNumRegexGroups.search('My number is (415) 555-4242').group(1))

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
print(batRegex.search('Batmobile lost a wheel'))

batRegex = re.compile(r'Bat(wo)?man')
print(batRegex.search('The Adventures of Batwoman'))

phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
print(phoneNumRegex.search('My number is 415-555-4242'))

batRegex = re.compile(r'Bat(wo)*man')
print(batRegex.search('The Adventures of Batwowowoman'))

batRegex = re.compile(r'Bat(wo)+man')
print(batRegex.search('The Adventures of Batman'))

regex = re.compile(r'\+\*\?')
print(regex.search('I learned about +*? regex syntax'))

regex = re.compile(r'(\+\*\?)+')
print(regex.search('I learned about +*?+*?+*?+*?+*?+*? regex syntax'))

haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('He said "HaHaHa'))

haRegex = re.compile(r'(Ha){3,5}')
print(haRegex.search('He said "HaHaHaHa'))

phoneNumRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneNumRegex.findall('My number is 415-555-4242. His number is 415-555-1234'))

lyrics = "12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping 9 Ladies Dancing \
        8 Maids a Milking 7 Swans a Swimming 6 Geese a Laying 5 Golden Rings \
        4 Calling Birds 3 French Hens 2 Turtle Doves and 1 Partridge in a Pear Tree"

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Hello friend'))

vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(vowelRegex.findall('Helloo friend'))

vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('Hello friend'))


beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))

endsWithWorld = re.compile(r'world!$')
print(endsWithWorld.search('Hello world!'))

allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search('1238478912376378954789'))
print(allDigitsRegex.search('123847891237x378954789'))

atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Cameron Last Name: Wohlfeil'))

serve = '<To serve humans> for dinner.>'
non_greedy = re.compile(r'<(.*?)>')
print(non_greedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dotStar = re.compile(r'.*')
print(dotStar.search(prime))
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))

vowelRegex = re.compile(r'[aeiou]', re.I)
print(vowelRegex.findall(prime))

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob'))

namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob'))
print(namesRegex.sub(r'Agent \1******', 'Agent Alice gave the secret documents to Agent Bob'))

phoneNumRegex = re.compile(r'''
\d\d\d      #Area code
-
\d\d\d      #First 3 digits
-
\d\d\d\d    #Last 4 digits
''', re.VERBOSE | re.IGNORECASE)
print(phoneNumRegex.search('My number is 415-555-4242'))
