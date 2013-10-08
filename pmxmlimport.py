import argparse
import dateutil.parser
from lxml import etree

def parse_pmxl(pmxml):
	tagmapping = {
		'mfh' : 'measfileheader',
		'md' : 'measdata',
		'mff' : 'measfilefooter'		
	}
	mdc = dict()
	md = dict()
	tree = etree.parse(pmxml)
	root = tree.getroot()
	for elem in tree:
		if elem.tag ==  'mfh':
			mdc[tagmapping[mfh]] = parse_mfh(elem)
		elif elem.tag == 'md':
			# parse_md(elem)
			# Check if nedn exists in md[nedn]
			# if it already exists, append result to list found at md[nedn]
			# else create a new hash entry at md[nedn]. Create a new list as the value of md[nedn]. Add result to list.
		elif elem.tag == 'mff':
			mdc[tagmapping[mff]] = parse_mff(elem)
	mdc[tagmapping[md]] = md

def parse_mfh(elem):
	tagmapping = {
		'ffv' : 'fileformatversion',
		'sn' : 'sendername',
		'st' : 'sendertype',
		'vn' : 'vendorname',
		'cbt' : 'collectionbegintime'	
	}
	mfh = dict()
	for child in elem:
		if child.tag == 'cbt':
			mfh[tagmapping[child.tag]] = dateutil.parser.parse(child.text)
		elif child.tag in tagmapping:
			mfh[tagmapping[child.tag]] = child.text
	return mfh



def parse_md(elem):
	pass

def parse_mff(elem):
	pass

def main():
	parser = argparse.ArgumentParser(description='Parse 3GPP TS 32.432 performance measurement collection data XML files into JSON format.')
	parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, metavar='FILE_TO_PARSE', help='Path to PM XML file to parse.')
	args = parser.parse_args()
	for pmxml file in args.file:
		parse_pmxl(pmxml)

if __name__ == '__main__':
	main()