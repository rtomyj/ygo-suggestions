import pymysql
from collections import defaultdict

from card import Card
from ygo_regex import *
import db

dbConn = pymysql.connect(host='localhost', user='root', passwd='', database='yugioh_API_DB')
dbCursor = dbConn.cursor()

sql = 'select card_name, card_effect from cards'
dbCursor.execute(sql)
rows = dbCursor.fetchall()

cards = list()
for row in rows:
    cards.append(Card(card_name=row[0], card_effect=row[1]))

references = defaultdict(set)
for card in cards:
    matches = CARD_REFERENCE.findall(card.card_effect)
    for match in matches:
        match = match.replace('"', '')
        if match != card.card_name:  # card referencing itself isn't important, only adding references of other cards
            references[card.card_name].add(match)

print(references)
print(len(references))

directReferences = defaultdict(set)
for card_name, refs in references.items():
    for card in cards:
        if card.card_name in refs:
            directReferences[card_name].add(card.card_name)
            refs.remove(card.card_name)

print(directReferences)
print(len(directReferences))
print(references)

db.cleanup(dbConn, dbCursor)