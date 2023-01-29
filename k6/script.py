import os, sys

print("\n Select One from the following URL")
url_dict = {
	1: 'zite.zite.io',
	2: 'app.zite.io',
	3: 'cfp.zite.io',
	4: 'www.commonfeedbackplatform.org'
}

method_dict = {
	1: 'GET',
	2: 'POST'
}
print(f"1). {url_dict[1]}")
print(f"2). {url_dict[2]}")
print(f"3). {url_dict[3]}")
print(f"4). {url_dict[4]}")

inp = int(input("Please Enter a number: "))
if inp not in [1, 2, 3, 4]:
	print('INVALID INPUT')
	sys.exit()

print("\n Select One from the following Method")
print(f"1). {method_dict[1]}")
# print("2). POST")

inm = int(input("Please Enter a number: "))
if inm not in [1]:
	print("INVALID INPUT")
	sys.exit()

inpt = input("Enter token for user: ")

os.system(f"k6 run -e BASEURL={url_dict[inp]} -e METHOD={method_dict[inm]} -e TOKEN={inpt} get-test.js")
sys.exit()

