import re

def verify(condition):
    if condition:
        print("Macth found")
    else:
        print("No match")

sample_text = "sdadfs5fd676sf"

starts_with = re.search("^sd", sample_text) # '^' Check if sample_text starts with "sd"
ends_with = re.search("$sd", sample_text) # '$' Check if sample_text ends  With "sd"
exact_occurence = re.search("sd{2}", sample_text) # '{n}' Check if sample_text has "sd" exactly n numver of times
any_vowel = re.search("[a,e,i,o,u]", sample_text) # '[]' Check if sample_text has any of these characters "a,e,i,o,u"
any_digits = re.search("\d",sample_text) # '\d' Check if sample_text has any digits
find_digits = re.findall("\d",sample_text)# '\d' Find all digits in sample_text

verify(starts_with)
verify(ends_with)
verify(exact_occurence)
verify(any_vowel)
verify(any_digits)
print(find_digits)
