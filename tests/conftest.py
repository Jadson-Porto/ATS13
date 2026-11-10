import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.gerenciador_recursos import GerenciadorRecursosMarte

@pytest.fixture(scope="module")
def parametros_iniciais_habitat():
    return {"oxigenio_inicial": 500.0, "agua_inicial": 1000.0}

@pytest.fixture(scope="function")
def gerenciador(parametros_iniciais_habitat):
    instancia = GerenciadorRecursosMarte(
        oxigenio_inicial=parametros_iniciais_habitat["oxigenio_inicial"],
        agua_inicial=parametros_iniciais_habitat["agua_inicial"]
    )
    yield instancia
    instancia.oxigenio = 0
    instancia.agua = 0

@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # O Selenium 4+ gerencia o driver automaticamente
    browser = webdriver.Chrome(options=options)
    yield browser

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        browser.save_screenshot(f"evidencia_{request.node.name}.png")
    
    browser.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)