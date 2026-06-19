from dataclasses import dataclass

# pra evitar criar muitos metodos na mão, eu uso o
# dataclass que já me dá de graça equals, toString e init
@dataclass
class Contact:
    name: str
    phone: str