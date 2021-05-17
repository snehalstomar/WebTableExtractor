import requests
import pandas as pd
import os
import argparse
import time
import progressbar

def table_reader(url):
	widgets = ['Processing: ', progressbar.AnimatedMarker()]
	bar = progressbar.ProgressBar(widgets=widgets).start()

	html = requests.get(url).content
	df_list = pd.read_html(html)
	nom = url.split("//")[-1].split("/")[1]
	os.mkdir(nom)
	count = 0
	for i in df_list:
		df = i
		filename = nom + "/" + str(count + 1) + ".csv"
		df.to_csv(filename)
		count = count + 1
		bar.update(count)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--url", help="url from which tables have to be extracted")
	args = parser.parse_args()
	table_reader(args.url)				