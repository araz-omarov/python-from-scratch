Name = "Araz Omarov"
words = ["Araz", "Omarov"]

print(Name.upper())                 # "ARAZ OMAROV"   ---> Araz Omarov = ARAZ OMAROV
print(Name.lower())                 # "araz omarov"   ---> Araz Omarov = araz omarov
print(Name.title())                 # "Araz Omarov"   ---> Araz Omarov = Araz Omarov
print(Name.strip())                 # "Araz Omarov"   ---> Araz Omarov = Araz Omarov
print(Name.replace("Araz","Tunar")) # "Tunar Omarov"  ---> Araz Omarov = Tunar Omarov
print(len(Name))                    # "11"            ---> Araz Omarov's long's = 11
print(Name.split())                 # ['Araz', 'Omarov'] ---> Araz Omarov = ['Araz', 'Omarov']
print(" ".join(words))              # "Araz Omarov"   ---> ['Araz', 'Omarov'] = Araz Omarov