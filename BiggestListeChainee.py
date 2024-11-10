class Maillon :
    """Classe qui modélise un maillon d'une liste chainee"""    
    def __init__(self, val, suiv=None):
        """Maillon, Objet, Maillon -> Maillon
        Construit un maillon d'une liste chainee"""
        self.__val = val
        self.__suiv = suiv
    
    def get(self):
        """Maillon -> Objet
        
        >>> m = Maillon(1)
        >>> m.get()
        1
        >>> m2 = Maillon(2, m)
        >>> m2.get()
        2
        >>> m2.suivant().get()
        1"""
        return self.__val
    
    def suivant(self):
        """Maillon -> Maillon
        
        >>> m = Maillon(1)
        >>> m.suivant()
        >>> m2 = Maillon(2, m)
        >>> m2.suivant().get()
        1"""
        return self.__suiv
    
    def set_suiv(self, m):
        """Maillon, Maillon -> None
        
        >>> m = Maillon(1)
        >>> m/set_suiv(Maillon(2))
        >>> m.suivant().get()
        2"""
        self.__suiv = m

    def __str__(self):
        """Maillon -> str
        
        >>> m = Maillon(1)
        >>> print(m)
        1
        >>> m2 = Maillon(2, m)
        >>> print(m2)
        2"""
        mess = str(self.__val)
        if self.__suiv != None :
            mess += ', '
        return mess

class ListeChainee :
    """Classe qui modélise une liste sous la forme recursive d'une liste chainee"""
    def __init__(self):
        """ListeChainee -> ListeChainee
        Une liste est toujours initialisee a la liste vide"""
        self.__tete = None
    
    def est_vide(self):
        """ListeChainee -> boolean
        
        >>> l = ListeChainee()
        >>> l.est_vide()
        True
        >>> l.append(1)
        >>> l.est_vide()
        False"""
        return self.__tete == None
    
    def append(self, val):
        """ListeChainee, Objet -> None
        
        >>> l = ListeChainee()
        >>> print(l)
        []
        >>> L.append(1)
        >>> print(l)
        [1]
        >>> l.append(2)
        >>> l.append(3)
        >>> print(l)
        [1, 2, 3]
        """
        if self.est_vide():
            self.__tete = Maillon(val)
        else :
            #prec : maillon auquel on va raccrocher le nouveau maillon
            prec = self.__tete
            while prec.suivant() != None :
                prec = prec.suivant()
            prec.set_suiv(Maillon(val))
        
    def __str__(self):
        """ListeChainee -> str
        
        >>> l = ListeChainee()
        >>> print(l)
        []
        >>> l.append(1)
        >>> print(l)
        [1]
        >>> l.append(2)
        >>> l.append(3)
        >>> print(l)
        [1, 2, 3]
        >>> l.len()
        3"""
        mess = "["
        prec = self.__tete
        while prec != None:
            mess += prec.__str__()
            prec = prec.suivant()
        mess += "]"
        return mess
    
    def len(self):
        """ListeChainee -> int
        
        >>> l = ListeChainee()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.len()
        3"""
        nb = 0
        prec = self.__tete
        while prec != None:
            prec = prec.suivant()
            nb += 1
        return nb

    def get(self, ind):
        """ListeChainee, int -> Objet
        
        >>> l = ListeChainee()
        >>> l.append(1)
        >>> l.get(0)
        1
        >>> l.append(2)
        >>> l.append(3)
        >>> l.get(2)
        2
        >>> l.get(2)
        3"""
        assert self.__tete != None
        cpt = 0
        m = self.__tete
        while cpt < ind:
            assert m.suivant() != None
            m = m.suivant()
            cpt += 1
        return m.get()
    
    def delete(self, ind):
        """ListeChainee, int -> None
        
        >>> l = ListeChainee()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.delete(1)
        >>> print(l)
        [1, 3]
        >>> l.delete(0)
        >>> print(l)
        [3]"""
        assert ind < self.len()
        if ind == 0:
            self.__tete = self.__tete.suivant()
        else :
            prec = self.__tete
            for i in range(ind-1):
                prec = prec.suivant()
            prec.set_suiv(prec.suivant().suivant())
    
    def insert (self, val, ind):
        """ListeChainee, Objet, int -> None
        
        >>> l = ListeChainee()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> print(l)
        [1, 2, 3]
        >>> l.insert(8, 0)
        >>> print(l)
        [8, 1, 12, 2, 3]
        >>> l.insert(15, 4)
        >>> print(l)
        [8, 1, 12, 15, 3]"""
        assert ind < self.len()
        if ind == 0:
            self.__tete = Maillon(val, self.__tete)
        else :
            prec = self.__tete
            for i in range(ind-1):
                prec = prec.suivant()
            prec.set_suiv(Maillon(val, prec.suivant()))
    
    def ajoute_maillon(self, m):
        """ListeChainee, Maillon -> None
        
        >>> lc = ListeChainee()
        >>> lc.append(-1), lc.append(5), lc.append(-3), lc.append(-8), lc.append(14)
        >>> m = Maillon(5)
        >>> lc.ajoute_maillon(m)
        >>> print(lc)
        [-1, 5, -3, -8, 14, 5]
        >>> lc.supprimer_maillon(m)
        >>> print(lc)
        [-1, 5, -3, -8, 14]"""
        if self.est_vide():
            self.__tete = m
        else :
            prec = self.__tete
            while prec.suivant() != None :
                prec = prec.suivant()
            prec.set_suiv(m)
    
    def supprimer_maillon(self, m):
        """ListeChainee, Maillon -> None
        
        >>> lc = ListeChainee()
        >>> lc.append(-1), lc.append(5), lc.append(-3), lc.append(-8), lc.append(14)
        >>> m = Maillon(5)
        >>> lc.ajoute_maillon(m)
        >>> print(lc)
        [-1, 5, -3, -8, 14, 5]
        >>> lc.supprimer_maillon(m)
        >>> print(lc)
        [-1, -3, -8, 14]"""
        if self.__tete != None:
            if self.__tete == m:
                self.__tete = self.__tete.suivant()
            else :
                prec = self.__tete
                while prec != None and prec.suivant() != m:
                    prec = prec.suivant()
                if prec != None:
                    prec.set_suiv(m.suivant())
    
    def ajoute_liste(self, liste):
        """Construit une liste chainée à partir d'une liste passée en paramètre
        
        >>> lc = ListeChainee()
        >>> lc.ajoute_liste([1, 12, 3, 8, 14])
        >>> print(lc)
        [1, 12, 3, 8, 14]"""
        assert self.est_vide()
        self.__tete = Maillon(liste[0])
        prec = self.__tete
        for i in range(1, len(liste)):
            m = Maillon(liste[i])
            prec.set_suiv(m)
            prec = prec.suivant()
    
    def plus_grand(self, n, m):
        """Calcule la plus grande valeur d'un intervalle de la liste
        
        >>> lc = ListeChainee()
        >>> lc.ajoute_liste([1, 12, 3, 8, 14])
        >>> print(lc)
        [1, 12, 3, 8, 14]
        >>> lc.plus_grand(3, 9)
        8"""
        assert not self.est_vide() and n < m
        trouve = False
        prec = self.__tete
        mawi = None
        while prec != None:
            if n <= prec.get() <= m:
                if not trouve:
                    maxi = prec.get()
                    trouve = True
                elif maxi < prec.get():
                    maxi = prec.get()
        return maxi
        
    
    def supprimer_negatifs(self):
        """Supprime les éléments négatifs de la liste
        
        >>> lc = ListeChainee()
        >>> lc.append(-1), lc.append(12), lc.append(-3), lc.append(-8), lc.append(14)
        >>> lc.supprimer_negatifs()
        >>> print(lc)
        [12, 14]"""
        if self.__tete != None:
            prec = self.__tete
            pos = 0
            while prec != None:
                if prec.get() < 0:
                    prec = prec.suivant()
                    self.delete(pos)
                else :
                    prec = prec.suivant()
                    pos += 1
    
    def supprimer_doublons(self):
        """Supprime les doublons de la liste
        
        >>> lc = ListeChainee()
        >>> lc.append(1), lc.append(12), lc.append(3), lc.append(8), lc.append(14), lc.append(3)
        >>> lc.supprimer_doublons()
        >>> print(lc)
        [1, 12, 3, 8, 14]"""
        if self.__tete != None:
            l = []
            prec = self.__tete
            l.append(prec.get())
            while prec != None and prec.suivant() != None:
                if prec.suivant().get() in l:
                    prec.set_suiv(prec.suivant().suivant())
                else :
                    prec = prec.suivant()
                    l.append(prec.get())
    
    def supprimer(self, n, m):
        """Supprime les n maillons après les premiers m maillons
        
        >>> lc = ListeChainee()
        >>> lc.ajoute_liste([1, 12, 3, 8, 14])
        >>> print(lc)
        [1, 12, 3, 8, 14]
        >>> lc.supprimer(1, 2)
        [1, 8, 12, 14]"""
        assert n > 0 and m > 0 and n + m >= self.len()
        prec1 = self.__tete
        for i in range(m -1):
            prec1 = prec1.suivant()
        prec2 = prec1
        for i in range(n + 1):
            prec2 = prec2.suivant()
        prec1.set_suiv(prec2)
    
    def set(self, ind, val):
        assert 0 <= ind < self.len()
        prec = self.__tete
        for i in range(ind):
            prec = prec.suivant()
        prec.set_suiv(Maillon(val, prec.suivant()))
    
    def permute(self, k):
        """Permute l'élément à la kième position depuis le début avec à la position k depuis la fin
        
        >>> lc = ListeChainee()
        >>> lc.ajouter_liste([1, 12, 3, 8, 14])
        >>> print(lc)
        [1, 12, 3, 8, 14]
        >>> lc.permute(1)
        [1, 8, 3, 12, 14]"""
        n = self.len()
        assert 0 <= k < n
        val = self.get()
        self.set(k, self.get(n - k - 1))
        self.set(n - k - 1, val)

    def intersection(self, lc):
        """Permet de trouve un maillon d'intersection de deux liste chainées"""
        n = self.len()
        m = lc.len()
        diff = n - m
        prec1 = self.__tete
        prec2 = lc.__tete
        if diff > 0:
            for i in range(diff):
                prec1 = prec1.suivant()
        else :
            for i in range(-diff):
                prec2 = prec2.suivant()
        while prec1 != None:
            if prec1 == prec2:
                return True
            prec1 = prec1.suivant()
            prec2 = prec2.suivant()
        return None

    def inverser(self):
        """Inverse la liste chainée
        
        >>> lc = ListeChainee()
        >>> c.ajoute_liste([1, 12, 1, 8, 1, 5, 9, 8, 0])
        >>> print(lc)
        [1, 12, 1, 8, 1, 5, 9, 8, 0]
        >>> lc.inverser()
        [0, 8, 9, 5, 1, 8, 1, 12, 1]"""
        if self.__tete == None or self.__tete.suivant() == None:
            return
        prec = None
        courant, suivant = self.__tete, self.__tete
        while courant != None:
            suivant = courant.suivant()
            courant.set_suiv(prec)
            prec = courant
            courant = suivant
        self.__tete = prec
    
    def fusion(self, liste1, liste2):
        """Fusionne deux listes chainées triées. Utilisert le même principe que le tri fusion vu en cours
        
        >>> lc = ListeChainee()
        >>> lc.ajoute_liste([1, 12, 3, 8, 14])
        >>> lc2 = ListeChainee()
        >>> lc2.ajoute_liste([1, 2, 3, 4, 5])
        >>> lc3 = ListeChainee()
        >>> lc3.fusion(lc, lc2)
        >>> print(lc3)
        [1, 1, 2, 3, 3, 4, 5, 8, 12, 14]"""
        if self.__tete == None:
            self = lc
        elif lc.__tete != None:
            if self.__tete.get() > lc.__tete.get():
                self,lc = lc,self
        courant = self.__tete
        suivant = lc.__tete
        prec = courant
        while courant != None:
            if courant.get() <= suivant.get():
                prec = courant
                courant = courant.suivant()
            else:
                prec.set_suiv(suivant)
                courant,suivant = suivant,courant
            if suivant != None:
                prec.set_suiv(suivant)
    
    def appartient(self, val):
        """Teste si une val donnée est pésente dans la liste chainée
        
        >>> l = listeChainee()
        >>> l.ajoute_liste([2, 4, 7, 2, 0])
        >>> l.appartient(2)
        True
        >>> l.appartient(8)
        False"""
        prec = self.__tete
        while prec != None:
            if prec.get() == val:
                return True
            prec = prec.suivant()
        return False
    
    def nb_occ(self, val):
        """Calcule le nombre d'occurence d'une valeur donnée dans la liste chainée
        
        >>> l = listeChainee()
        >>> l.ajoute_liste([2, 4, 7, 2, 0])
        >>> l.nb_occ(2)
        2
        >>> l.nb_occ(8)
        0"""
        prec = self.__tete
        nb = 0
        while prec != None:
            if prec.get() == val:
                nb += 1
            prec = prec.suivant()
        return nb
    
    def val_max(self):
        """Calcule la valeur maximale de la liste chainée
        
        >>> l = listeChainee()
        >>> l.ajoute_liste([2, 4, 7, 2, 0])
        >>> l.val_max()
        7"""
        prec = self.__tete
        maxi = prec.get()
        while prec != None:
            if prec.get() > maxi:
                maxi = prec.get()
            prec = prec.suivant()
        return maxi
    
    def indices_min(self):
        """Retourne les indices des maillons de valeur minimale d'une liste chainée d'entiers
        
        >>> l = listeChainee()
        >>> l.ajoute_liste([2, 0, 7, 2, 0])
        >>> l.indices_min()
        [1, 4]"""
        prec = self.__tete
        mini = prec.get()
        indices = []
        pos = 0
        while prec != None:
            if prec.get() < mini:
                mini = prec.get()
                indices = [pos]
            elif prec.get() == mini:
                indices.append(pos)
            prec = prec.suivant()
            pos += 1
        return indices

    def permute_tete_queue(self):
        """Permutte la tete et la queue d'une liste chainée
        
        >>> l = listeChainee()
        >>> l.ajoute_liste([2, 0, 7, 2, 0])
        >>> l.permute_tete_queue()
        >>> print(l)
        [0, 0, 7, 2, 2]"""
        prec = self.__tete
        while prec.suivant() != None:
            prec = prec.suivant()
        prec.set_suiv(self.__tete)
        self.__tete = self.__tete.suivant()
        prec.suivant().set_suiv(None)
    
    def premier_repetition(self):
        """Trouve le premier élément qui se répềte dans une liste chainée
        
        >>> l = listeChainee()
        >>> l.ajoute_liste([2, 0, 7, 7, 0])
        >>> l.premier_repetition()
        7"""
        prec = self.__tete
        l = []
        while prec != None:
            if prec.get() in l:
                return prec.get()
            l.append(prec.get())
            prec = prec.suivant()
        return None
    
    def supprimer_paires(self):
        """Supprimer la moitié des maillons. Ceux à supprimer sont des maillons de rang paires
        
        >>> l = listeChainee()
        >>> l.ajoute_liste([2, 4, 7, 2, 0])
        >>> print(l)
        [2, 4, 7, 2, 0]
        >>> l.supprimer_paires()
        >>> print(l)
        [4, 2]"""
        prec = self.__tete
        while prec != None and prec.suivant() != None:
            prec.set_suiv(prec.suivant().suivant())
            prec = prec.suivant()
    
    def contient_rec(self, val):
        """Teste si un valeur donnée est présente dans une liste chainée
        
        >>> lc = ListeChainee()
        >>> lc.ajoute_liste([1, 2, 10, 5, 0])
        >>> lc.contient_rec(7)
        False"""
        if self.__tete is None:
            return False
        if self.__tete.get() == val:
            return True
        reste_liste = ListeChainee()
        reste_liste.__tete = self.__tete.suivant()
        return reste_liste.contient_rec(val)
    
    def indice_minimum_rec(self):
        """Retourne les indices des maillons de valeur minimale d'une liste chainée
        
        >>> lc = listeChainee()
        >>> lc.ajoute_liste([1, -2, 10, 5, -2])
        >>> lc.indice_minimum_rec()
        [1, 4]"""
        pass

    def permute_pairs_rec(self):
        """Permute chaques deux maillons qui se suivent
        
        >>> lc = listeChainee()
        >>> lc.ajoute_liste([1, -2, 10, 5, -2, 5, 12, 10])
        >>> lc.permute_pairs_rec()
        >>> print(lc)
        [-2, 1, 5, 10, 5, -2, 10, 12]"""
        pass

    def division_rec(self):
        """Divise une liste chainée en deux listes chainées en attribuant les maillons a tour de rôle"""
        pass





#################################################################################################################################################################






class ListeChaineeRec:
    def __init__(self):
        """ListeChaineeRec -> ListeChaineeRec"""
        self.__tete = None

    def len(self):
        """ListeChaineeRec -> int"""
        if self.est_vide():
            return 0
        else :
            return self.__tete.len()
    
    def append(self, val):
        """ListeChaineeRec (inout), Objet -> None
        
        >>> l = ListeChaineeRec()
        >>> print(l)
        []
        >>> l.append(1)
        >>> print(l)
        [1]
        >>> l.append(2)
        >>> l.append(3)
        >>> print(l)
        [1, 2, 3]"""
        if self.est_vide():
            self.__tete = MaillonRec(val)
        else :
            self.__tete.append(val)
    
    def get(self, ind):
        """ListeChaineeRec, int -> Objet
        
        >>> l = ListeChaineeRec()
        >>> l.append(1)
        >>> l.get(0)
        1
        >>> l.append(2)
        >>> l.append(3)
        >>> l.get(1)
        2
        >>> l.get(2)
        3"""
        assert ind < self.len()
        return self.__tete.get(ind)
    
    def set(self, ind, val):
        """ListeChaineeRec, int, Objet -> None
        
        >>> l = ListeChaineeRec()
        >>> l.append(1)
        >>> l.get(0)
        1
        >>> l.set(0, 5)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.get(2)
        3
        >>> l.set(2, 10)
        >>> print(l)
        [5, 2, 10]"""
        assert ind < self.len()
        self.__tete.set(ind, val)

    def delete(self, ind):
        """ListeChainneeRec, int, None
        
        >>> l = ListeChaineeRec()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> l.delete(0)
        >>> print(l)
        [1, 3]
        >>> l.delete(0)
        >>> print(l)
        [3]"""
        assert ind < self.len()
        if ind == 0:
            self.__tete = self.__tete.suivant()
        else :
            self.__tete.delete(ind - 1)
    
    def insert(self, val, ind):
        """Liste!chaineeRec, Objetn int -> None
        
        >>> l = ListeChaineeRec()
        >>> l.append(1)
        >>> l.append(2)
        >>> l.append(3)
        >>> print(l)
        [1, 2, 3]
        >>> l.insert(8, 0)
        >>> print(l)
        [8, 1, 2, 3]
        >>> l.insert(12, 2)
        >>> print(l)
        [8, 1, 12, 2, 3]
        >>> l.insert(15, 4)
        >>> print(l)
        [8, 1, 12, 2, 15, 3]"""
        assert ind < self.len()
        if ind == 0:
            self.__tete = MaillonRec(val, self.__tete)
        else :
            self.__tete.insert(val, ind - 1)
    
    def copy(self):
        """ListeChaineeRec -> ListeChaineeRec"""
        l = ListeChaineeRec()
        if not self.est_vide():
            l.__tete = self.__tete.copy()
        return l

class MaillonRec:
    def __init__(self, val, suiv = None):
        """MaillonRec, Objet, MaillonRec -> MaillonRec"""
        self.__val = val
        self.__suiv = suiv
    
    def len(self):
        """MaillonRec -> int"""
        if self.__suiv == None:
            return 1
        else :
            return 1 + self.__suiv.len()
        
    def __str__(self):
        """MaillonRec -> str
        
        >>> m = MaillonRec(1)
        >>> print(m)
        1
        >>> m2 = MaillonRec(2, m)
        >>> print(m2)
        2, 1"""
        mess = str(self.__val)
        if self.__suiv != None:
            mess += ", " + self.__suiv.__str__()
        return mess
    
    def append(self, val):
        """MaillonRec, Objet -> None"""
        if self.__suiv == None:
            self.__suiv = MaillonRec(val)
        else :
            self.__suiv.append(val)
    
    def get(self, ind):
        """MaillonRec, ind -> Objet"""
        assert ind < self.len()
        if ind == 0:
            return self.__val
        else :
            return self.__suiv.get(ind - 1)
    
    def set(self, ind, val):
        """MaillonRec (inout), int, Objet -> None"""
        assert ind < self.len()
        if ind == 0:
            self.__val = val
        else :
            self.__suiv.set(ind - 1, val)
    
    def delete(self, ind):
        """MaillonRec, int -> None"""
        assert ind < self.len()
        if ind == 0:
            self.__suiv = self.__suiv.__suiv
        else :
            self.__suiv.delete(ind - 1)
    
    def insert(self, val, ind):
        """MaillonRec, Objet, int -> None"""
        assert ind < self.len()
        if ind == 0:
            self.__suiv = MaillonRec(val, self.__suiv)
        else :
            self.__suiv.insert(val, ind - 1)
    
    def copy(self):
        """MaillonRec -> MaillonRec"""
        m = MaillonRec(self.__val)
        if self.__suiv is not None:
            m.__suiv = self.__suiv.copy()
        return m
    
