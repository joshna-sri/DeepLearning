Dictionary = {"English": ["food", "travel", "speak"],
              "Telugu": ["Aaharam", "Prayaṇaṁ", "Māṭlāḍatāru"],
              "Tamil": ["Uṇavu", "Payaṇam", "Pēcu"],
              "Malayalam": ["bhakshanam", "yaathra", "samsaarikkuka"],
              "Kannada": ["AhAra", "PrayAṇa", "Mātanāḍuttāre"]}
e2_value =input("please enter a string")
for i in Dictionary.keys():
    if e2_value == Dictionary.key[0][i]:
        telugu = Dictionary["Telugu"][i]
        tamil = Dictionary["Tamil"][i]
        malayalam = Dictionary["Malayalam"][i]
        kannada = Dictionary["Kannada"][i]
        print(telugu)
        print(tamil)
        print(malayalam)
        print(kannada)

