citta_grandi = [
["Tokyo",37339804],
["Delhi",31181376],
["Shanghai",27795702],
["Sao Paulo",22237472],
["Mexico City",21918936],
["Dhaka",21741090],
["Cairo",21322750],
["Beijing",20896820],
["Mumbai",20667656],
["Osaka",19110616],
["Karachi",16459472],
["Chongqing",16382376],
["Istanbul",15415197],
["Buenos Aires",15257673],
["Kolkata",14974073],
["Kinshasa",14970460],
["Lagos",14862111],
["Manila",14158573],
["Tianjin",13794450],
["Guangzhou",13635397],
["Rio de Janeiro",13544462],
["Lahore",13095166],
["Bangalore",12764935],
["Moscow",12593252],
["Shenzhen",12591696],
["Chennai",11235018],
["Bogota",11167392],
["Paris",11078546],
["Jakarta",10915364],
["Lima",10882757],
["Bangkok",10722815],
["Hyderabad",10268653],
["Seoul",9967677],
["Nagoya",9565642],
["London",9425622],
["Chengdu",9305116],
["Tehran",9259009],
["Nanjing",9143980],
["Ho Chi Minh City",8837544],
["Luanda",8631876],
["Wuhan",8473405],
["Xi-an Shaanxi",8274651],
["Ahmedabad",8253226],
["New York City",8230290],
["Kuala Lumpur",8210745],
["Hangzhou",7845501],
["Hong Kong",7598189],
["Surat",7489742],
["Dongguan",7451889],
["Suzhou",7427096],
["Foshan",7406751],
["Riyadh",7387817],
["Shenyang",7373655],
["Baghdad",7323079],
["Dar es Salaam",7046892],
["Santiago",6811595],
["Pune",6807984],
["Madrid",6668865],
["Haerbin",6526439],
["Toronto",6254571],
["Belo Horizonte",6139774],
["Singapore",5991801],
["Khartoum",5989024],
["Johannesburg",5926668],
["Dalian",5775938],
["Qingdao",5742486],
["Barcelona",5624498],
["Fukuoka",5516158],
["Ji-nan Shandong",5513597],
["Zhengzhou",5510341],
["Saint Petersburg",5504305],
["Yangon",5421806],
["Alexandria",5381101],
["Abidjan",5354826],
["Guadalajara",5259296],
["Ankara",5215747],
["Chittagong",5132751],
["Melbourne",5061439],
["Addis Ababa",5005524]]

def citta_pop_min(listacitta, minpop = 7000000):

     lista_out=[]
     for citta in listacitta:
         if citta[1]>minpop:
             lista_out.append(citta[0])

     return lista_out


def citta_per_intervallo_popolazione(listacitta, intervallo):
     lista_out=[]
     for citta in listacitta:
         if citta[1]>intervallo[0] and citta[1]<intervallo[1]:
             lista_out.append(citta[0])

     return lista_out

lista = citta_pop_min(minpop = 10000000, listacitta = citta_grandi)
print(len(lista))
print(lista)

intervallo67 = [6000000, 7000000]

lista = citta_per_intervallo_popolazione(citta_grandi, intervallo67)
print(len(lista))
print(lista)

l1 = citta_per_intervallo_popolazione(listacitta = citta_grandi, intervallo = intervallo67)
