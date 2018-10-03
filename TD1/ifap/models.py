from django.db import models


class Classe(models.Model):
    classe_name = models.CharField(max_length = 30)
    
    def _str_(slef):
        return self.classe

class Ordre(models.Model):
    classe = models.ForeignKey(Classe, on_delete = models.CASCADE)
    ordre_name = models.CharField(max_length = 30)

    def _str_(slef):
        return self.ordre

class Famille(models.Model):
    ordre = models.ForeignKey(Ordre, on_delete = models.CASCADE)
    famille_name = models.CharField(max_length = 30)

    def _str_(slef):
        return self.famille

class Animal(models.Model):
    famille = models.ForeignKey(Famille, on_delete = models.CASCADE)
    cummun_name = models.CharField(max_length = 50)
    sc_name = models.CharField(max_length = 50)

    def _str_(slef):
        return self.animal

        
