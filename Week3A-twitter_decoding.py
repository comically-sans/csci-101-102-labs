# Dominic Pergola
# CSCI 102 - Section H
# Week 3 - Part A
# Reference: zybooks for base code
# Time ~10 minutes

print("Enter the Tweet or Message abbreviation to decode.")
tweet = input('TWEET> ')

if tweet == 'LOL':
    print(f'The decoded abbreviation is:\nOUTPUT {tweet} = laugh out loud')
elif tweet == 'BFN':
    print(f'The decoded abbreviation is:\nOUTPUT {tweet} = bye for now')
elif tweet == 'FTW':
    print(f'The decoded abbreviation is:\nOUTPUT {tweet} = for the win')
elif tweet == 'IRL':
    print(f'The decoded abbreviation is:\nOUTPUT {tweet} = in real life')
elif tweet == 'BTW':
    print(f'The decoded abbreviation is:\nOUTPUT {tweet} = by the way')
elif tweet == 'DM':
    print(f'The decoded abbreviation is:\nOUTPUT {tweet} = direct message')
elif tweet == 'IDK':
    print(f"The decoded abbreviation is:\nOUTPUT {tweet} = I don't know")
elif tweet == 'AFAIK':
    print(f'The decoded abbreviation is:\nOUTPUT {tweet} = as far as I know')
elif tweet == 'TTYL':
    print(f'The decoded abbreviation is:\nOUTPUT {tweet} = talk to you later')
elif tweet == 'LMK':
    print(f'The decoded abbreviation is:\nOUTPUT {tweet} = let me know')
else:
    print("Sorry, don't know that one")
