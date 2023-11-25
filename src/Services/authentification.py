from DAO.authentificationDAO import AuthentificationDAO


class Authentification:
    def verifier(self, id_user, mdp):
        verify = AuthentificationDAO().verification(id_user, mdp)
        return verify


# if __name__ == "__main__":
#     Authentification().verifier()
