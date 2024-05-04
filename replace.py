h = open('h.txt', 'r')
h1 = h.read()
h.close()

h = open('h.txt', 'w')
h.write(h1.replace("Less than ₹5,00,000", '1').replace('₹5,00,000 - ₹9,99,999', '2').replace('₹10,00,000 - ₹14,99,999', '3').replace('₹15,00,000 - ₹24,99,999', '4').replace('₹25,00,000 - ₹49,99,999', '5').replace('₹50,00,000 or more', '6').replace('Prefer not to answer', '7'))
h.close()