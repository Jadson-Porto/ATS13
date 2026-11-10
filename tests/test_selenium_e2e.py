import pathlib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_solicitacao_cota_oxigenio_e2e(driver):
    caminho_html = pathlib.Path(__file__).parent.parent / "web" / "painel.html"
    driver.get(f"file://{caminho_html.resolve()}")

    wait = WebDriverWait(driver, 10)
    campo_qtd = wait.until(EC.presence_of_element_located((By.ID, "quantidade")))
    btn_solicitar = driver.find_element(By.ID, "btn-solicitar")

    campo_qtd.send_keys("50")
    btn_solicitar.click()

    mensagem_status = wait.until(
        EC.visibility_of_element_located((By.ID, "mensagem-status"))
    )
    nivel_oxigenio = driver.find_element(By.ID, "nivel-oxigenio")

    assert mensagem_status.text == "Cota solicitada com sucesso!"
    assert nivel_oxigenio.text == "150.0"