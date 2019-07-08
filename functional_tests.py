from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitor(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edith va sur l'appli
        self.browser.get("http://localhost:8000")

        # Y a marqué "Todo list" dans le titre
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-do", header_text)

        # On l'invite à rentrer un todo dans un champ de texte
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # Elle saisit "Me faire foutre" dans une text box
        inputbox.send_keys("Buy peacock feathers")

        # Quand elle appuie sur entrée, la page se met à jour et la page affiche sa liste d'items
        # "1: Aller me faire foutre" comme item dans un table de to do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])

        # Il y a toujours un champ texte qui lui permet d'ajhouter des éléments à sa liste
        # Elle saisit "Aller dormir"
        table = self.browser.find_element_by_id("id_list_table")
        inputbox.send_keys("Manger ses morts")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # La page se met de nouveau à jour et affiche tous ses éléments
        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])
        self.assertIn("2: Manger ses morts", [row.text for row in rows])

        # Elle se demande si le site se souviendra de sa liste quand elle va la quitter.
        self.fail("Finish the test!")

        # Elle s'aperçoit qu'on lui propose un URL perso pour se rendre sur son site.

        # Elle visite cette URL et retrouve sa liste.

        # Heureuse, elle retourne vivre sa vie misérable


if __name__ == "__main__":
    unittest.main()
