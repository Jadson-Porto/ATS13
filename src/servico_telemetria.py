class ServicoTelemetriaEspacial:
    """Dependência externa responsável pela comunicação com a Terra."""
    def enviar_relatorio_status(self, dados: dict) -> bool:
        return True

    def disparar_alerta_crise(self, mensagem: str) -> bool:
        return True