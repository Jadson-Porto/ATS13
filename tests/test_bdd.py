from pytest_bdd import scenarios, given, when, then, parsers
from src.gerenciador_recursos import GerenciadorRecursosMarte

scenarios('../features/solicitacao_oxigenio.feature')

@given(parsers.parse('que o gerenciador possui {quantidade:d} litros de oxigênio'), target_fixture='contexto_bdd')
def iniciar_gerenciador(quantidade):
    return {'gerenciador': GerenciadorRecursosMarte(oxigenio_inicial=float(quantidade), agua_inicial=500.0)}

@when(parsers.parse('o astronauta solicita {quantidade:d} litros de cota extra'))
def solicitar_cota(contexto_bdd, quantidade):
    contexto_bdd['gerenciador'].solicitar_cota_extra(float(quantidade))

@then(parsers.parse('o saldo total de oxigênio deve ser {quantidade:d} litros'))
def verificar_saldo(contexto_bdd, quantidade):
    assert contexto_bdd['gerenciador'].oxigenio == float(quantidade)