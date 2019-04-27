from .init import onEmptyCards

from aqt.main import AnkiQt
from aqt import mw
# def onEmptyCards(self):
#     print("new on empty cards")
#     pass
AnkiQt.onEmptyCards = onEmptyCards
mw.form.actionEmptyCards.triggered.disconnect()
mw.form.actionEmptyCards.triggered.connect(mw.onEmptyCards)
