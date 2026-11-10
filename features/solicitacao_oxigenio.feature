Feature: Solicitação de Cota Extra de Oxigênio

  Scenario: Solicitar oxigênio em condições normais
    Given que o gerenciador possui 100 litros de oxigênio
    When o astronauta solicita 50 litros de cota extra
    Then o saldo total de oxigênio deve ser 150 litros