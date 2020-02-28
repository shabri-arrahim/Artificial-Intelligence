import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
from itertools import islice
from itertools import accumulate
from sklearn.model_selection import train_test_split

###########################Data Validation###################################
#Meng-import file TXT dan dijadikan sebagai array 
def Data(filename):
	with open(filename) as txtfile:
		readTXT = pd.read_csv(txtfile, delimiter='\t', header=None)
		Data = readTXT
	return Data.to_numpy()

###########################Decision Tree With Genetic Argorithm###################################
#Generate populasi berdasarkan parameter yg telah ditentukan
def GeneratePopulation(n_pop, n_rule, r_bound):
	population = np.zeros(n_pop, dtype=object)
	for i in range(n_pop):
		r_rule = n_rule*np.random.randint(r_bound[0], r_bound[1])
		population[i] = np.random.randint(2, size=(r_rule))
	return population

#Decode DNA menjadi rule yang sesuai dengan data set
def DecodeKromosom(pop, split_v):
	# count = 0
	x_value = np.zeros(len(pop), dtype=object)
	for i in range (len(pop)):
		post = np.split(pop[i], pop[i].size/15)
		# print(post)
		y_value = np.zeros(len(post), dtype=object)
		for k in range(len(y_value)):
			y_value[k] = np.asarray([post[k][x - y: x] for x, y in zip(accumulate(split_v), split_v)])
		x_value[i] = y_value
	for i in range(len(x_value)):
		for j in range(len(x_value[i])):
			for k in range(len(x_value[i][j])):
				x_value[i][j][k] = x_value[i][j][k].astype(str)
	for i in range(len(x_value)):
		for j in range(len(x_value[i])):
			for k in range(len(x_value[i][j])):
				for l in range(len(x_value[i][j][k])):
					if(k == 0 or k == 3): 
						if(l == 0):
							if(x_value[i][j][k][l] == '1'):
								x_value[i][j][k][l] = 'Rendah' 
						if(l == 1):
							if(x_value[i][j][k][l] == '1'):
								x_value[i][j][k][l] = 'Normal'
						if(l == 2):
							if(x_value[i][j][k][l] == '1'):
								x_value[i][j][k][l] = 'Tinggi'
					if(k == 1): 
						if(l == 0):
							if(x_value[i][j][k][l] == '1'):
								x_value[i][j][k][l] = 'Pagi'
						if(l == 1):
							if(x_value[i][j][k][l] == '1'):
								x_value[i][j][k][l] = 'Siang'
						if(l == 2):
							if(x_value[i][j][k][l] == '1'):
								x_value[i][j][k][l] = 'Sore'
						if(l == 3):
							if(x_value[i][j][k][l] == '1'):
								x_value[i][j][k][l] = 'Malam'
					if(k == 2): 
						if(l == 0):
							if(x_value[i][j][k][l] == '1'):
								x_value[i][j][k][l] = 'Cerah'
						if(l == 1):
							if(x_value[i][j][k][l] == '1'):
								x_value[i][j][k][l] = 'Berawan'
						if(l == 2):
							if(x_value[i][j][k][l] == '1'):
								x_value[i][j][k][l] = 'Rintik'
						if(l == 3):
							if(x_value[i][j][k][l] == '1'):
								x_value[i][j][k][l] = 'Hujan'
					if(k == 4): 
						if(l == 0):
							if(x_value[i][j][k][l] == '1'):
								x_value[i][j][k][l] = 'Ya'
							else: x_value[i][j][k][l] = 'Tidak'
	return x_value

#Mengitung nilai fitnes dari populasi terhadap data train
def Fitnes(falue, data) :
	x = data[:, :-1]
	y = data[:, -1]
	x_train, x_Test, y_train, y_test = train_test_split(x, y, test_size=0.1)
	akurasi = np.zeros([len(falue)], dtype=int)
	for pop in range(len(falue)):
		for j in range(len(falue[pop])):
			arr = np.zeros(len(falue[pop]), dtype=int)
			benar = 0
			suhu = falue[pop][j][0]
			waktu = falue[pop][j][1]
			kondisi = falue[pop][j][2]
			lembab = falue[pop][j][3]
			terbang = falue[pop][j][4]
		for i in range(len(x_train)):
			if(suhu[0] == x_train[i][0] or suhu[1] == x_train[i][0] or suhu[2] == x_train[i][0]) :
				if(waktu[0] == x_train[i][1] or waktu[1] == x_train[i][1] or waktu[2] == x_train[i][1] or waktu[3] == x_train[i][1]) :
					if(kondisi[0] == x_train[i][2] or kondisi[1] == x_train[i][2] or kondisi[2] == x_train[i][2] or kondisi[3] == x_train[i][2]) :
						if(lembab[0] == x_train[i][3] or lembab[1] == x_train[i][3] or lembab[2] == x_train[i][3]) :
							if(terbang[0] == y_train[i]):
								benar += 1
		arr[j] = benar
		akurasi[pop] = arr.sum()
	return (akurasi*20)/data.size


def Selection(fitness):
    i = 0
    kumfit = 0
    while i < len(fitness):
        kumfit = kumfit + fitness[i]
        if (kumfit/fitness.sum()) > np.random.uniform(0,1):
            index = i
            break
        i=i+1
    index = i
    return index

def CrossOver(parent1, parent2, CROSS_RATE):
	calonTPparent2 = []
	cPointP1 = np.random.randint(0, len(parent1), size=2)
	if cPointP1[0]>cPointP1[1] :
		cPointP1[0],cPointP1[1]=cPointP1[1],cPointP1[0]
	MaxlenghtParent2 = len(parent2)
	
	cPointP2 = np.zeros(2, dtype=int)
	temp1 = np.zeros(2, dtype=int)
	temp2 = np.zeros(2, dtype=int)

	cPointP2[0] = cPointP1[0]%15
	cPointP2[1] = cPointP1[1]%15

	if cPointP2[0]>cPointP2[1] :
		cPointP2[0],cPointP2[1]=cPointP2[1],cPointP2[0]

	calonTPparent2.append(cPointP2)
	
	# MaxPoint2= 0
	# count1 = 0
	# while count1 < MaxlenghtParent2:
	# 	temp1[0] = cPointP2[0]
	# 	temp1[1] = cPointP2[1] + 15
	# 	calonTPparent2.append(temp1)
	# 	count1 = count1+15
	# 	MaxPoint2 = count1

	# temp2[0] = temp1[0]
	# count1 = 0
	# while count1 < MaxPoint2:
	# 	temp2[0] = cPointP2[0] + 15
	# 	temp2[1] = cPointP2[1]
	# 	calonTPparent2.append(temp2)
	# 	count1 = MaxPoint2+15

	if np.random.rand() < CROSS_RATE :
		Idx_tipot = np.random.randint(0, len(calonTPparent2))
		tipotP2 = calonTPparent2[Idx_tipot]

		if tipotP2[0]>tipotP2[1] :
			cPointP2[0],cPointP2[1]=cPointP2[1],cPointP2[0]

		child1 = np.concatenate((parent1[:cPointP1[0]], parent2[tipotP2[0]:tipotP2[1]],parent1[tipotP2[1]:]), axis=None) #[parent1[:cPointP1[0]], parent2[tipotP2[0]:tipotP2[1]], parent2[tipotP2[1]:]]
		child2 = np.concatenate((parent2[:tipotP2[0]], parent1[cPointP1[0]:cPointP1[1]], parent2[cPointP1[1]:]), axis=None) #[parent2[:tipotP2[0]], parent1[cPointP1[0]:cPointP1[1]], parent1[cPointP1[1]:]]
		return child1, child2
	else:
		return parent1, parent2

def Mutate(child1, child2, MUTATION_RATE):
    for idx in range(len(child1)):
        if np.random.rand() < MUTATION_RATE:
            child1[idx] = 1 if child1[idx] == 0 else 0
    for idx in range(len(child2)):
        if np.random.rand() < MUTATION_RATE:
            child2[idx] = 1 if child2[idx] == 0 else 0
    return child1, child2

def tebakan(data, split_v):
	file = open('output.txt', 'w')
	Cromosomterbaik = np.array([1,1,1,1,1,1,1,1,0,1,1,1,1,0,0])
	array = np.zeros(1, dtype=object)
	array[0] = Cromosomterbaik
	falue=DecodeKromosom(array, split_v)
	x = data[:]
	x_train = x
	akurasi = np.zeros([len(falue)], dtype=int)
	for pop in range(len(falue)):
		for j in range(len(falue[pop])):
			arr = np.zeros(len(falue[pop]), dtype=int)
			benar = 0
			suhu = falue[pop][j][0]
			waktu = falue[pop][j][1]
			kondisi = falue[pop][j][2]
			lembab = falue[pop][j][3]
			terbang = falue[pop][j][4]
		for i in range(len(x_train)):
			if(suhu[0] == x_train[i][0] or suhu[1] == x_train[i][0] or suhu[2] == x_train[i][0]) :
				if(waktu[0] == x_train[i][1] or waktu[1] == x_train[i][1] or waktu[2] == x_train[i][1] or waktu[3] == x_train[i][1]) :
					if(kondisi[0] == x_train[i][2] or kondisi[1] == x_train[i][2] or kondisi[2] == x_train[i][2] or kondisi[3] == x_train[i][2]) :
						if(lembab[0] == x_train[i][3] or lembab[1] == x_train[i][3] or lembab[2] == x_train[i][3]) :
							file.write('1')
						else:
							file.write('0')
					file.write('\n')
		file.close()

def main():
	#Mengakses file text
	namefile = 'G:\APPL\AI\GA [For Decission Tree]\DataTrain.txt'
	data_test = 'G:\APPL\AI\GA [For Decission Tree]\DataTest.txt'
	pre_data = Data(namefile)
	data = Data(data_test)
	N_Generation = 200
	N_POPULATION = 10
	N_RULE = 15
	R_BOUND = [1, 2]
	split_value = [3, 4, 4, 3, 1]
	CROSS_RATE = 0.8
	MUTATION_RATE = 1.6

	Populasi = GeneratePopulation(N_POPULATION, N_RULE, R_BOUND)
	for i in range (N_Generation):
		value = DecodeKromosom(Populasi, split_value)
		place_idx1 = np.random.randint(1, len(value))
		place_idx2 = np.random.randint(1, len(value))
		fit_value = Fitnes(value, pre_data)
		print("Generasi {:<5s}: ".format(str((i+1))), max(fit_value), Populasi[np.argmax(fit_value)])
		idx_p1 = Selection(fit_value)
		idx_p2 = Selection(fit_value)
		p1 = Populasi[idx_p1]
		p2 = Populasi[idx_p2]
		anak_1 = CrossOver(p1, p2, CROSS_RATE)
		child_1 = anak_1[0]
		child_2 = anak_1[1]
		anak = Mutate(child_1, child_2, MUTATION_RATE)
		child1 = anak[0]
		child2 = anak[1]
		Populasi[place_idx1]=child1
		Populasi[place_idx2]=child2

	# untuk melihat hasil tebakan Data
	tebakan(data, split_value)



if __name__ == '__main__':
	main()