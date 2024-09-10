count = 99
while count > 1:
     print(f"   {count} bottles of beer on the wall,\n{count} bottles of beer \ntake one down \npass it around \n{count} bottles of beer on the wall.")
     count -= 1
while count == 1:
     print(f"   {count} bottle of beer on the wall,\n{count} bottle of beer \ntake one down \npass it around \nno more bottles of beer on the wall")
     count -= 1
     break