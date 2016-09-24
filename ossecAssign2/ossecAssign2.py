#!/usr/bin/python
import crypt
import sys
import os.path
import spwd
import pwd
import hashlib

def main():
 user = input('Enter the username: ')
 temp = open("dictionary", "r")	
 dict = "" 
 for line in temp:
	dict = dict + temp.readline()		

try:
	entry = pwd.getpwnam(user)[1]
 	if entry:
    		print "Username " + user + " is found"
    		hash = spwd.getspname(user)[1]

	if h:
		if h == '*':
       			print "User has a blank password"
		else: 
			print "The hash for " + user + " is: " + hash
			print "Finding password for user: " + user
			define(entry)
			compare(h, dict)
	else:
		print "User not found."
except: KeyError

def compare(h, dict):
	for line in dict:
		h = encrypt(line, alg)
		if h == hash:
			string = "Password: %s" % (line)
			print(string)
			break
		else:
			print "Password was not found in dictionary"
	return;


def defineAlg(entry):
	entry = entry[1:]
	entry = isdigit(entry)
	return;

def encrypt(word, alg):
	if alg == 1:
		print "MD5 was used"
		hash = hashlib.md5(word).hexdigest()
	elif alg == 5:
		print "SHA-256 was used"
		hash = hashlib.sha256(word).hexdigest()
	elif alg == 6:
		print "SHA-512 was used"
		hash = hashlib.sha512(word).hexdigest()
	else:
		print "Invalid hashing algorithm"
	return;
