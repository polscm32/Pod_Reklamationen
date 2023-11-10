#!/usr/bin/env python3 

count = 0

# save pod complainings in an empty list
pod_summaries = []

# put it all in a while loop to do the same for every pod
while True: 
    count += 1

    print(f"Hallo! Ich helfe dir dabei, deinen Pod zu reklamieren! (Reklamation Nr. {count})\n")
   
    # numbers
    pd_number = input("Welche PD Nummer hatte dein Pod?\n")
    other_number = input("Welche andere Nummer hatte dein Pod?\n")

    # place
    place = input("Wo hast du deinen Pod gesetzt?\n")
   
    # date of insertion
    date = input("Wann hast du deinen Pod gesetzt?\n")
   
    # blood sugar changes
    sugar = input("Gab es Blutzuckerveränderungen? [y/n]\n")
    
    if sugar.lower() == "y":
        high = input("Wie hoch stieg der Blutzucker?\n")

    # skin reactions?
    skin = input("Gab es Hautveränderungen? [y/n]\n")
   
    # regular pod changes? successful pod change?
    change = input("Wechselst du regelmäßig deinen Pod [y/n]?\n")
    new_pod = input("Hast du erfolgreich einen neuen Pod angebracht [y/n]?\n")
    
    # medical assistance necessary?
    help = input("Brauchtest du medizinische Unterstützung [y/n]?\n")

    # summary of pod
    pod_summary = {
        "Zusammenfassung Pod": count,
        "Nummern": f"{pd_number}, {other_number}",
        "Setzstelle": place,
        "Datum": date,
        "Blutzuckerveränderungen": "Es gab keine Blutzuckerveränderungen" if sugar.lower() == "n" else f"Der Blutzucker stieg bis auf {high}",
        "Erfolgen regelmäßige Pod-Wechsel?": "Ja" if change.lower() == "y" else "Nein",
        "Wurde ein neuer Pod erfolgreich gesetzt?": "Ja" if new_pod.lower() == "y" else "Nein",
        "Wurde medizinische Unterstützung benötigt?": "Ja" if help.lower() == "y" else "Nein"
    }

    pod_summaries.append(pod_summary)

    go_on = input("Möchtest du einen weiteren Pod reklamieren [y/n]?\n\n")

    if go_on.lower() == "n":
        break

#summary at the end of user input
if count > 1:
    print("\nZusammenfassungen der reklamierten Pods:\n")
else:
    print("Dann fasse ich deine Reklamation zusammen:\n")

for i, summary in enumerate(pod_summaries, start=1):
    for key, value in summary.items():
        print(f"{key}: {value}")
