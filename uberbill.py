#uber bill program
bikerate=100
Autorate=200
Minirate=300
Microrate=400
Primerate=500
sourcefrom=['guindy'.upper(),'velacherry'.upper(),'Medavakkam'.upper(),'potheri'.upper()]
Destinationto=['koyambedu'.upper(),'vadapalani'.upper(),'perungulathur'.upper(),'tnagar'.upper()]
modoftrans=['bike'.upper(),'Auto'.upper(),'Mini'.upper(),'Micro'.upper(),'Prime'.upper()]
inp=str(input("Enter the source :"))
inp2=str(input("Enter the destination :"))
inp3=str(input("Mode of Transport :"))
while(1==1):
 if(inp.upper() in sourcefrom) and (inp2.upper() in Destinationto) and(inp3.upper() in modoftrans):
  if(inp3.upper()=='bike'.upper()):
    print('Need to pay'|bikerate|'enjoy your uber ride')
    break
  elif(inp3.upper()=='Auto'.upper()):
    print('Need to pay' + str(Autorate) + 'enjoy your uber ride')
    break
  elif(inp3.upper()=='Mini'.upper()):
    print('Need to pay'+ str(Minirate) + 'enjoy your uber ride')
    break
  elif(inp3.upper()=='Micro'.upper()):
    print('Need to pay' + str(Microrate) +'enjoy your uber ride')
    break
  else:
    print('Need to pay' + str(Primerate) +'enjoy your uber ride')
    break    
 else:
  print('Please select available routes/Mode of transport')
  inp=str(input("Enter the source :"))
  inp2=str(input("Enter the destination :"))
  inp3=str(input("Mode of Transport :"))

  