import re

file = open("dzo.txt", "r", encoding="utf-8") content = file.read(); file.close()

cleaned_content = content.translate(str.maketrans("", "", string.ascii_letters + string.digits + string.punctuation))

file = open("cleanedzo.txt", "w", encoding="utf-8") file.write(cleaned_content) file.close();

print("cleaned successfully")

#cleaning 




