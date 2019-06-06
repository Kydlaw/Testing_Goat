from selenium import webdriver
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
        self.fail("Finish the test!")

        # On l'invite à rentrer un todo dans un champ de texte

        # Elle saisit "Me faire foutre"

        # Quand elle appuie sur entrée, la page se met à jour et la page affiche sa liste d'items

        # Il y a toujours un champ texte qui lui permet d'ajhouter des éléments à sa liste
        # Elle saisit "Aller dormir"

        # La page se met de nouveau à jour et affiche tous ses éléments

        # Elle se demande si le site se souviendra de sa liste quand elle va la quitter.
        # Elle s'aperçoit qu'on lui propose un URL perso pour se rendre sur son site.

        # Elle visite cette URL et retrouve sa liste.

        # Heureuse, elle retourne vivre sa vie misérable


if __name__ == "__main__":
    unittest.main()
