import string

freq_english = [
        0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228,
        0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
        0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987,
        0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
        0.01974, 0.00074
    ]

cypertext = """
    serdhrapln anylfvfvfn shaqnzragn ygrpuavdhr hfrqvapelc gnanylfvfg
    bqrpvcurer apelcgrqzr ffntrfcneg vphyneylgu bfrrapelcg rqhfvatfvz
    cyrfhofgvg hgvbapvcur efguronfvp cerzvfrbss erdhraplna nylfvfyvrf
    vagursnpgg ungpregnva yrggrefbef lzobyfnccr nezberserd hragylvant
    viraynathn trgunabgur efolnanylm vatgurserd hraplbsgur frpunenpgr
    efjvguvana rapelcgrqz rffntrpelc gnanylfgfp naznxrrqhp ngrqthrffr
    fnobhggurf hofgvghgvb afhfrqvagu rrapelcgvb acebprff
    """.replace("\n", "").replace(" ", "").lower()


length = len(cypertext)
count = [0]*26
for i in cypertext:
    if i in string.ascii_lowercase:
        idx = ord(i) - ord('a')
        count[idx] += 1
        

freq_alphabet = [i / length for i in count]

best_score = -1
best_k = -1

for k in range(26):
    score_k = 0.0
    for i in range(26):
        score_k += freq_alphabet[(i+k)%26] * freq_english[i]
    
    if best_score < score_k:
        best_score = score_k
        best_k = k


plantext = ""

for j in cypertext:
    if j in string.ascii_lowercase:
        idx = ord(j) - ord('a')
        plantext += string.ascii_lowercase[(idx + best_k) % 26]



print("Best k: ", best_k)
print("Best score: ", best_score)
print("Ciphertext: ", cypertext)
print("Plaintext: ", plantext)