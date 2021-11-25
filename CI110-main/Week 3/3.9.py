# User inputs
en, hww = input('Enter Employee\'s name: '),\
    eval(input('Enters number of hours worked in a week: '))
hpr, fwr = eval(input('Enter hourly pay rate: ')),\
    eval(input('Enter federal tax withholding rate: '))
swr = eval(input('Enter stae tax withholding rate: '))

# Math
gp = hww * hpr
fw, sw = fwr * gp, swr * gp
d = fw + sw
td = fw + sw
np = gp - d

print('\nEmployee Name: {} \nHours worked: {}\nPay Rate: ${}\nGross pay: ${}'.format(
    en, format(hww, ".2f"), format(hpr, ".2f"), format(gp, ".2f")), end="\nDeductions:")
print('\n\tFederal Withholding ({}): ${}'.format(
    format(fwr, ".1%"), format(fw, ".2f")))
print('\tState Withholding (' + format(swr, ".1%") + '): $' + format(sw, ".2f"))
print('\tTotal Deduction: $' + format(td, ".2f"))
print('Net Pay: $' + format(np, ".2f"))
