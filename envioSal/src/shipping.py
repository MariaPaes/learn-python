def envio():
  print ("ATENCAO: se o valor do peso for decimal, utilize o '.' para fazer a separacao.\n")
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
    print("\nO transporte mais barato e o Drone com o custo de ", cost_Drone, " libras\n")

  elif cost_Premium < cost_Drone and cost_Premium < cost_ground:
    print("\nO transporte mais barato e o terrestre PREMIUM com o custo de ", cost_Premium, " libras\n")
    
  elif cost_ground < cost_Drone and cost_ground < cost_Premium:
    print("\nO transporte mais barato e o TERRESTRE com o custo de ", cost_ground, " libras\n")
  
  return weight, cost_ground, cost_Drone, cost_Premium

def transportsValue(weight, cost_ground, cost_Drone, cost_Premium):
  while True:
    outrosTransportes = input("\n------\nBuscar outras transportadoras? Responda com S (para sim) ou N (para nao): ")
    if outrosTransportes == "S":
      print("\nO peso do pacote é de ", weight, " libras")
      print("\nO envio de transporte TERRESTRE tem o custo de ", cost_ground, " libras")
      print("\nO envio pelo DRONE tem o custo de ",cost_Drone, " libras")
      print("\nO envio de transporte terrestre PREMIUM tem o custo de ", cost_Premium, " libras")
      break
    elif outrosTransportes == "N":
      print("Ok!")
      break
    else:
      print("Não entendi. Repita!\n")

def reCalculo():
  while True:
    calcNov = input("\n---\nCalcular o transporte de outro produto? Responda com S (para sim) ou N (para nao): ")
    if calcNov == "S":
        weight, cost_ground, cost_Drone, cost_Premium = envio()
        transportsValue(weight, cost_ground, cost_Drone, cost_Premium)
    elif calcNov == "N":
        print("até a próxima")
        break
    else:
        print("Não entendi. Repita!")

weight, cost_ground, cost_Drone, cost_Premium = envio()
transportsValue(weight, cost_ground, cost_Drone, cost_Premium)
reCalculo()