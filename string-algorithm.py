from string import maketrans



# Uppercase
stringz = "string";
# print stringz.upper();



# # Capitalize
# print stringz.title();



#reverse a string
# print stringz[::-1]
newList = list(stringz)
reverseList = list(reversed(newList))
finalOutput = ''.join(reverseList)
print finalOutput




# LEET STRINGGGGGGG
# paragraph = 'Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):'
# paragraphUpper = paragraph.upper();
# intab = 'AEGIOST'
# outtab = '4361057'
# trantab = maketrans(intab,outtab)
# print paragraphUpper.translate(trantab)




# make vowels longggggggger
def longVowel(string):
	string = string.replace('ee','eeeee');
	string = string.replace('aa','aaaaa');
	string = string.replace('oo','ooooo');
	string = string.replace('ii','iiiii');
	string = string.replace('uu','uuuuu');						
	print string;

# longVowel('man'); longVowel('cheese'); longVowel('spoon'); longVowel('good')





# Caeser Cipher
decipherThis = 'lbh zhfg hayrnea jung lbh unir yrnearq'
intabCipher = 'abcdefghijklmnopqrstuvwxyz'
outtabCipher = 'nopqrstuvwxyzabcdefghijklm'
trantabCipher = maketrans(intabCipher,outtabCipher)
print decipherThis.translate(trantabCipher)

	

