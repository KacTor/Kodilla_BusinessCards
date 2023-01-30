from faker import Faker

fake = Faker()


class BaseContact:

    def __init__(self, firstName, lastName, phoneNumberPriv, mail):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumberPriv = phoneNumberPriv
        self.mail = mail

    def contact(self):
        return print(f'Wybieram numer {self.phoneNumberPriv} i dzwonię do {self.firstName} {self.lastName}.')

    def _len_of_name(self):
        return len(self.firstName), len(self.lastName)

    def __str__(self) -> str:
        return f'{self.firstName},{self.lastName},{self.phoneNumberPriv},{self.mail}'


class BusinessContact(BaseContact):

    def __init__(self, company, occupation, phoneNumberWork, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.occupation = occupation
        self.phoneNumberWork = phoneNumberWork

    def contact(self):
        return print(f'Wybieram numer {self.phoneNumberWork} i dzwonię do {self.firstName} {self.lastName}.')

    def _len_of_name(self):
        return len(self.firstName), len(self.lastName)

    def __str__(self) -> str:
        return f'{self.firstName}, {self.lastName}, {self.phoneNumberWork}, {self.company},{self.occupation}.'


def create_contacts(typeOfBusinessCard: str, amountOfCards) -> list:
    '''Return list.
    typeOfBusinessCard must be as string:
    'BaseContact' or 'BusinessContact'''
    listOfBusinessCards = []

    for _ in range(amountOfCards):
        firstName = fake.first_name()
        lastName = fake.last_name()
        phoneNumberPriv = fake.phone_number()
        mail = fake.ascii_email()
        company = fake.company()
        occupation = fake.job()
        phoneNumberWork = fake.phone_number()

        if typeOfBusinessCard == 'BaseContact':
            listOfBusinessCards.append(BaseContact(
                firstName, lastName, phoneNumberPriv, mail))

        elif typeOfBusinessCard == 'BusinessContact':
            listOfBusinessCards.append(BusinessContact(
                company, occupation, phoneNumberWork, firstName, lastName, phoneNumberPriv, mail,))

    return listOfBusinessCards


list = create_contacts('BaseContact', 3)
list2 = create_contacts('BusinessContact', 3)


for card in list:
    print(f'BaseCard: {card}')

for card in list2:
    print(f'BusinessCard: {card}')
