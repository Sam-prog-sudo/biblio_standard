import re

#------------------chercher dans une chaine-----------------#

re.search(r"abc", "abcdef")
# renvoie <_sre.SRE_Match object at 0x00AC1640>  ou None si ça n'existe pas

if re.match(expression, chaine) is not None:
    # Si l'expression est dans la chaîne
    # Ou alors, plus intuitivement
    pass
if re.match(expression, chaine):
    pass


# numéro de téléphone
#  ^0[0-9]([ .-]?[0-9]{2}){4}$
# ^ on cherche l'espression '0' en debut de chaine
# on doit trouver un chiffre entre 0 et 9
# soit un espace, un point ou un tiret, de maniere optionnelle
# 2 chiffres accollés, compris entre 0 et 9
#le groupe de 2 chffres accolés et séparés, doit se retrouver 4 fois


chaine = ""
expression = r"^0[0-9]([ .-]?[0-9]{2}){4}$"
while re.search(expression, chaine) is None:
    chaine = input("Saisissez un numéro de téléphone (valide) :")


#---------------------remplacer une chaine------------------------#

# re.sub()  3 parametres: l'expression à rechercher, 
#                         par quoi remplacer cette expression,
#                         la chaîne d'origine.

re.sub(r"(ab)", r" \1 ", "abcdef")  # appeler nos groupes grâce à '\<numéro du groupe>'
' ab cdef'

#---------------------compilation------------------------#

# conserver votre expression régulière sous la forme d'un objet
chn_mdp = r"^[A-Za-z0-9]{6,}$"
exp_mdp = re.compile(chn_mdp)
mot_de_passe = ""
while exp_mdp.search(mot_de_passe) is None:
    mot_de_passe = input("Tapez votre mot de passe : ")