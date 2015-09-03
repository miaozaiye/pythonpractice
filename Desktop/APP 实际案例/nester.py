def print_lol(the_list,indent=1,level=0):
	'''这个函数有一个位置参数为 the_list,这可以是任何Python列表，其中包含或者不包含嵌套列表'''
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item,indent,level+1)
		else:
			if indent==0:
			    for tab_stop in range(level):
				    print('\t',end='')
			print(each_item)

movies=['yes','no',[1,2,['why','do it']]]
print_lol(movies)
print_lol(movies,0)


