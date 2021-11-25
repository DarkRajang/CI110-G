# Variables

# Pounds to Kilograms
ktp = 1
# Kilograms to Pounds
ptk = 20

# Header
print(format('Kilograms', "<15s") + format('Pounds', "10s") +
      format('   |   ') + format('Pounds', ">10s") + format('Kilograms', ">15s"))

for i in range(58):
    print('-', end="")
print()

# Math and format

for v in range(1, 101, 1):
    print(format(ktp, "<15d") + format((ktp * 2.2), "<10.1f"),
          format('  |      '), format(ptk, '<11d'), format(ptk / 2.2, "<15.2f"))
    ktp += 2
    ptk += 5
