#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as BSoup
from flask import Flask, request, jsonify


def get_detail_harga_ipay(driver):
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

def get_harga_ipay():
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

	driver=webdriver.Chrome() 
	driver.get('http://ipay.allreport.net/report/users/login')
	# Wait for 5 seconds
	time.sleep(5)
	assert 'WebReport' in driver.title

	# Login

	elem = driver.find_element_by_name('id')
	elem.send_keys(id_ipay)
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
	driver.get('http://ipay.allreport.net/report/produk/detail/AH')
	# Wait for 3 seconds
	# time.sleep(3)
	assert 'Webreport' in driver.title
	three = get_detail_harga_ipay(driver)

	#indosa
	driver.get('http://ipay.allreport.net/report/produk/detail/AII')
	# Wait for 3 seconds
	# time.sleep(3)
	assert 'Webreport' in driver.title
	indosat = get_detail_harga_ipay(driver)

	#xl
	driver.get('http://ipay.allreport.net/report/produk/detail/ARS')
	# Wait for 3 seconds
	# time.sleep(3)
	assert 'Webreport' in driver.title
	xl = get_detail_harga_ipay(driver)

	#tsel
	driver.get('http://ipay.allreport.net/report/produk/detail/ASS')
	# Wait for 3 seconds
	# time.sleep(3)
	assert 'Webreport' in driver.title
	tsel = get_detail_harga_ipay(driver)

	
	# driver.close()
	driver.quit()
	return jsonify(three=three,indosat=indosat,xl=xl,tsel=tsel)

def get_detail_portal(driver, array_num):
	bs_obj = BSoup(driver.page_source, 'html.parser')
	rows = bs_obj.find_all('table')[array_num].find('tbody').find_all('tr')
	detail_harga = []
	for row in rows:
		cells = row.find_all('td')

		# name = row.find('th').get_text()

		kode = cells[1].get_text()
		harga = cells[2].get_text()

		detail_harga.append([kode, harga])
	return detail_harga

def get_harga_portalpulsa():
	driver=webdriver.Chrome() 
	driver.get('https://portalpulsa.com/pulsa-reguler-murah/')
	# Wait for 5 seconds
	time.sleep(2)
	assert 'Daftar harga Pulsa Reguler All Operator' in driver.title
	axis = get_detail_portal(driver,0)
	indosat = get_detail_portal(driver,2)
	telkomsel = get_detail_portal(driver,4)
	three = get_detail_portal(driver,5)
	xl = get_detail_portal(driver,6)

	driver.quit()
	return jsonify(axis=axis,indosat=indosat,telkomsel=telkomsel,three=three,xl=xl)

app = Flask(__name__)


@app.route('/')
def index():
	return 'Yo, its working!'


@app.route('/ipay')
def ipay():
	harga_final = get_harga_ipay()
	return harga_final

@app.route('/portal')
def portal():
	harga_final = get_harga_portalpulsa()
	return harga_final


if __name__ == '__main__':
	app.run()
