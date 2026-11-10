import pytest
from src.gerenciador_recursos import (
    GerenciadorRecursosMarte,
    OxigenioInsuficienteError,
    NivelEmergenciaInvalidoError
)
from src.servico_telemetria import ServicoTelemetriaEspacial

@pytest.mark.parametrize("astronautas, taxa, consumo_esperado", [
    (2, 1.0, 10.0),
    (4, 1.5, 30.0),
    (1, 2.0, 10.0),
    (0, 1.0, 0.0),
])
def test_calcular_consumo_diario_parametrizacao(gerenciador, astronautas, taxa, consumo_esperado):
    resultado = gerenciador.calcular_consumo_diario(astronautas, taxa)
    assert resultado == consumo_esperado

def test_excecao_nivel_emergencia_invalido(gerenciador):
    with pytest.raises(NivelEmergenciaInvalidoError):
        gerenciador.calcular_consumo_diario(astronautas=3, taxa_emergencia=0)

def test_excecao_oxigenio_insuficiente(gerenciador):
    with pytest.raises(OxigenioInsuficienteError):
        gerenciador.consumir_oxigenio(9999.0)

def test_telemetria_dispara_alerta_em_crise(mocker):
    mock_telemetria = mocker.MagicMock(spec=ServicoTelemetriaEspacial)
    gerenciador = GerenciadorRecursosMarte(
        oxigenio_inicial=50.0,
        agua_inicial=100.0,
        telemetria=mock_telemetria
    )
    with pytest.raises(OxigenioInsuficienteError):
        gerenciador.consumir_oxigenio(100.0)

    mock_telemetria.disparar_alerta_crise.assert_called_once_with("Nível crítico de Oxigênio!")