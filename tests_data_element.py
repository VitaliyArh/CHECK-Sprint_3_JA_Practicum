# проба написания теста по вебинару
# Командой pip install faker -- устанавливаем библиотеку фейковых данных,
# для генерации рандомных\случайных данных, например названий емаил, фамилии, адреса и так далее.

from faker import Faker # После установки импортируем библиотеку faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions # as EC

faker = Faker() # определяем библиотеку faker

class TestStelarBurger: # напишем тестовый класс с понятным названием, и для Pytest важно чтобы первое слово было Test
	def test_registration(self, driver): # объявляем функцию регистрации (первое слово в тестах всегда test) и в качестве аргумента передаём ей фикстуру driver
		email = faker.email()
		print(email)
		name = faker.name()
		print(name)
		# приступаем к написанию регистрации в тесте
		# вызываем драйвер фикстуры -- driver -- и прописываем локатор кнопки "войти в аккаунт"
		# импортируем By
		driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click() # клик по кнопке "Войти в аккаунт"
		driver.find_element(By.XPATH, "//p[1]/a[text()='Зарегистрироваться']").click()  # клик по Зарегистрироваться)
		driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(name)  # ввести имя
		driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(email)  # ввести Email
		driver.find_element(By.XPATH, "//input[@type='password']").send_keys(123456)  # ввести пароль
		driver.find_element(By.XPATH, "//form/button[text()='Зарегистрироваться']").click()  # клик по кнопке Зарегистри
		reg = WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[@class='input__error text_type_main-default']"))).text
		# reg = driver.find_element(By.XPATH, "//p[@class='input__error']").text
		assert reg == "Такой пользователь уже существует"





