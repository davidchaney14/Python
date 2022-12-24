income = 71000
single_person_tax_allowance = 36800
tax_at_20_percent = income - single_person_tax_allowance
tax_at_40_percent = income - tax_at_20_percent

percent_tax_20 = tax_at_20_percent * .2
percent_tax_40 = tax_at_40_percent * .4

total_tax = percent_tax_20 + percent_tax_40

print(total_tax)