cards1 = [("9","d"),("q","d"),("7","k"),("10","k")]
cards2 = [("9","d"),("q","d"),("7","k"),("10","d")]
cards3 = [("k","d"),("q","d"),("j","h"),("a","h")]

highest_num = []
highest_letter = []

def card_winner(cards):
	suit = cards[0][1]
	for card in cards:
		if card[1] == suit:
			try:
				if isinstance(int(card[0]), int):
					card = (int(card[0]),card[1])
					highest_num.append(card)
			except Exception:
				highest_letter.append(card)
		
	if highest_num:
		card = max(highest_num)
		card = (str(card[0]),card[1])
		print(cards.index(card))
	else:
		print(cards.index(min(highest_letter)))




card_winner(cards3)
