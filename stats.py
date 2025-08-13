def counter(text):
   print(text)
   newtext = text.split()
   lent = len(newtext)
   return lent+5
def charcount(text):
   text = text.lower()
   char_dict = {}

   for char in text:
      if char in char_dict:
         char_dict[char]+=1
      else:
         char_dict[char] = 1
    
   return char_dict
def ssort(d):
    newdict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    for key, value in list(newdict.items())[1:]:
     print(f"{key} : {value}")

