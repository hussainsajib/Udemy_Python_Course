temps = [ 221, 234, 340, -9999, 230 ]
new_temps = [ temp / 10 for temp in temps if temp != -9999]
new_temps2 = [ temp / 10 if temp != -9999 else 0 for temp in temps]
print(new_temps)
print(new_temps2)