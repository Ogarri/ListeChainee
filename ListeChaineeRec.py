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
            
    def est_vide(self):
        return self.__tete == None
        
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
    
