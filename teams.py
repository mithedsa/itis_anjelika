import datetime

class Abonents:
    def __init__(self, lastname: str, name: str, middle_name: str, birsthday: datetime.date, gender: str, connection_date:
    datetime.date, balance: float, tarif: str):
        """
        Constructor for Abonents class. Inits class properties
        :param lastname: operator's subscriber surname
        :param name: operator's subscriber name
        :param middle_name: operator's subscriber middle name
        :param birsthday: operator's subscriber birsday. Format: yyyy, m, d
        :param gender: gender: male or female
        :param connection_date: format: yyyy, m, d
        :param balance: balance counter
        :param tarif: name of tarif
        """
        self.lastname = lastname
        self.name = name
        self.middle_name = middle_name
        self.birsthday = birsthday
        self.gender = gender
        self.connection_date = connection_date
        self.balance = balance
        self.tarif = tarif
