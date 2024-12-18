
print ("ATENCAO: se o valor do peso for decimal, utilize o '.' para fazer a separacao.")
weight = float(input("Insira o peso do seu pacote em lb: "))

if weight <= 2:
  cost_ground = weight * 1.5 + 20
  cost_Drone = weight * 4.5
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
  cost_Drone = weight * 9
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
  cost_Drone = weight * 12
else:
  cost_ground = weight * 4.75 + 20
  cost_Drone = weight * 14.25

cost_Premium = 125
if cost_Drone < cost_ground and cost_Drone < cost_Premium:
  print("O transporte mais barato e o Drone com o custo de ", cost_Drone, " libras")

elif cost_Premium < cost_Drone and cost_Premium < cost_ground:
  print("O transporte mais barato e o terrestre PREMIUM com o custo de ", cost_Premium, " libras")
  
elif cost_ground < cost_Drone and cost_ground < cost_Premium:
  print("O transporte mais barato e o TERRESTRE com o custo de ", cost_ground, " libras")




#   ### BÔNUS
#   print("O envio de um pacote com ", weight, " libras de transporte TERRESTRE tem o custo de ", cost_ground, " libras")
# print("O envio de um pacote com ", weight, " libras, transportado pelo DRONE tem o custo de ",cost_Drone, " libras")
# print("O envio de um pacote com ", weight, " libras de transporte terrestre PREMIUM tem o custo de ", cost_Premium, " libras")
  