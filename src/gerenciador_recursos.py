class OxigenioInsuficienteError(Exception):
    pass

class NivelEmergenciaInvalidoError(Exception):
    pass

class GerenciadorRecursosMarte:
    def __init__(self, oxigenio_inicial: float, agua_inicial: float, telemetria=None):
        self.oxigenio = oxigenio_inicial
        self.agua = agua_inicial
        self.telemetria = telemetria

    def calcular_consumo_diario(self, astronautas: int, taxa_emergencia: float = 1.0) -> float:
        if taxa_emergencia <= 0:
            raise NivelEmergenciaInvalidoError("A taxa de emergência deve ser maior que zero.")
        consumo_base = 5.0
        return astronautas * consumo_base * taxa_emergencia

    def consumir_oxigenio(self, quantidade: float):
        if quantidade > self.oxigenio:
            if self.telemetria:
                self.telemetria.disparar_alerta_crise("Nível crítico de Oxigênio!")
            raise OxigenioInsuficienteError("Quantidade requerida excede o estoque disponível.")
        self.oxigenio -= quantidade
        return self.oxigenio

    def solicitar_cota_extra(self, quantidade: float) -> bool:
        if quantidade <= 0:
            return False
        self.oxigenio += quantidade
        return True