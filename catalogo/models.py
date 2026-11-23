from django.db import models


class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Plataforma(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    nome = models.CharField(max_length=150)
    ano_lancamento = models.PositiveIntegerField()
    desenvolvedora = models.ForeignKey(
        Desenvolvedora, on_delete=models.PROTECT, related_name='jogos'
    )
    plataforma = models.ForeignKey(
        Plataforma, on_delete=models.PROTECT, related_name='jogos'
    )

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome