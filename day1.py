import re

text = """Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC.This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32."""

#find text
text_find = re.search("This.*32.$",text)
print(text_find)


#check if there is "Lorem" in the text
text_find = re.findall("Lorem",text)
print(text_find)

#Split the string at every white-space character
text_find = re.split("\s",text)
print(text_find)

#Replace all white-space characters with the double white-space:
text_find = re.sub("\s","  ",text)
print(text_find)
