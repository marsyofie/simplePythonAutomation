#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as BSoup
from flask import Flask, request, jsonify


def get_detail_harga_tes(driver):
	bs_obj = BSoup(driver.page_source, 'html.parser')
	rows = bs_obj.find_all('table')[0].find('tbody').find_all('tr')
	detail_harga = []
	for row in rows:
		cells = row.find_all('td')

		# name = row.find('th').get_text()

		kode = cells[0].get_text()
		harga = cells[2].get_text()

		detail_harga.append([kode, harga])
	return detail_harga

def get_harga_tes():
	id_tes='xx'
	hp='+xx'
	pin='xx'
	

	# init
	#used for deploy on heroku
	# CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"

	# chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', "chromedriver")
	# options = webdriver.ChromeOptions()
	# options.binary_location = chrome_bin
	# options.add_argument("--disable-gpu")
	# options.add_argument("--no-sandbox")
	# options.add_argument('headless')
	# options.add_argument('window-size=1200x600')
	# driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
	#End used for deploy on heroku

	# driver=webdriver.Chrome('/app/.apt/usr/bin/google-chrome') 
	driver.get('xxx')
	# Wait for 5 seconds
	time.sleep(5)
	assert 'WebReport' in driver.title

	# Login

	elem = driver.find_element_by_name('id')
	elem.send_keys(id_tes)
	elem = driver.find_element_by_name('hp')
	elem.send_keys(hp)
	elem = driver.find_element_by_name('pass')
	elem.send_keys(pin)
	elem = driver.find_element_by_name('c')
	capcay = elem.get_attribute('value')
	elem = driver.find_element_by_name('b')
	elem.send_keys(capcay)
	elem.send_keys(Keys.RETURN)
	# Wait for 2 seconds
	time.sleep(2)

	#three
	driver.get('xx')
	# Wait for 3 seconds
	# time.sleep(3)
	assert 'Webreport' in driver.title
	three = get_detail_harga_tes(driver)

	#indosa
	driver.get('xx')
	# Wait for 3 seconds
	# time.sleep(3)
	assert 'Webreport' in driver.title
	indosat = get_detail_harga_tes(driver)

	#xl
	driver.get('xx')
	# Wait for 3 seconds
	# time.sleep(3)
	assert 'Webreport' in driver.title
	xl = get_detail_harga_tes(driver)

	#tsel
	driver.get('xx')
	# Wait for 3 seconds
	# time.sleep(3)
	assert 'Webreport' in driver.title
	tsel = get_detail_harga_tes(driver)

	
	# driver.close()
	driver.quit()
	return jsonify(three=three,indosat=indosat,xl=xl,tsel=tsel)

def get_detail_harga_duta(driver):
	bs_obj = BSoup(driver.page_source, 'html.parser')
	rows = bs_obj.find_all('table')[0].find_all('tr')
	detail_harga = []
	for row in rows:
		cells = row.find_all('td')

		# name = row.find('th').get_text()

		kode = cells[0].get_text()
		harga = cells[2].get_text()

		detail_harga.append([kode, harga])
	return detail_harga

app = Flask(__name__)


@app.route('/')
def index():
	return 'Yo, its working!'


@app.route('/tes')
def tes():
	harga_final = get_harga_tes()
	return harga_final


if __name__ == '__main__':
	app.run()
