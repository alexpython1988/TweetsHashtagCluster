import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import pickle


def multi_intra(cluster_num, data, process_num):
	pass

def multi_inter(cluster_num, data, process_num):
	pass

def main():
	cpu_num = multiprocessing.cpu_count() - 1

	with open("temp/1000cluster.pkl", "rb") as fr:
		gps = pickle.load(fr)

	multi_intra(11, gps, cpu_num)
	multi_inter(11, gps, cpu_num)

if __name__ == '__main__':
	main()