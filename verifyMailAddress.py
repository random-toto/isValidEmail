#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re

def isProperMail(mail=None):
    """ vérifie si l'input "mail" est valide """
    # On n'accepte que les str
    if type(mail) is not str:
        #~ print("Il ne s'agit pas d'une chaîne de caractères.")
        return False
    
    # On refuse les mails n'ayant pas d'@.
    if "@" not in mail:
        #~ print("Il n'y a pas d'arobase dans cette chaîne.")
        return False
    champs = mail.split('@')
    
    # On refuse les mails ayant plusieurs @ (cf méthode split).
    if len(champs) != 2:
        #~ print("pas le bon nombre de champs.")
        return False
    
    champ1 = champs[0]
    champ2 = champs[1]
    # On exige un . dans la deuxième partie de l'adresse
    if '.' not in champ2:
        #~ print("Pas de point dans la deuxième partie du 'mail'.")
        return False
    
    champs2 = champ2.split('.')
    
    # On n'accepte pas un . suivant l'@, ni rien après le point.
    if champs2[1] == "" or champs2[0] == "":
        #~ print("Rien avant ou après le point")
        return False

    # TLD acceptés. WARNING : ils y sont tous, sauf les réginonaux (.paris, ...) et les spéciaux (.vin, ...)
    regex = re.compile(r'(com|fr|net|biz|edu|gov|gouv|uk|de|be|tk|jp|cn|org|int|mil|arpa|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|ax|aw|az|ba|bb|bd|bf|bg|bh|bi|bj|bm|bn|bo|bq|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|co|cr|cs|cu|cv|cw|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|tf|tg|th|tj|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zr|zw)')
    #~ print(re.findall(regex, champs2[len(champs2)-1])) 
    if re.findall(regex, champs2[len(champs2)-1]) == []:
        #~ print("Pas un TLD reconnu")
        return False
    
    #~ print("Seems legit...")
    return True

#~ toto = input("Votre mail ? ")
#~ resultat = isProperMail(toto)
#~ print(resultat)
