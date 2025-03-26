# ? Similiar to spread(...) operator used in Javascript. Spread helps to unpack the elements of a list or a dictionary.Similiarly it unpacks all the key elements of the form.
# lst_one = [1, 2, 3]
# lst_two = [4, 5, 6, 7]
# lst = [0, *lst_one, *lst_two]
# print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
# country_lst_one = ['Finland', 'Sweden', 'Norway']
# country_lst_two = ['Denmark', 'Iceland']
# nordic_countries = [*country_lst_one, *country_lst_two]
# print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

#* Enumerate
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland'] 
for index, i in enumerate(countries):
    # print('hi')
    if(i == 'Finland'):
        print(f'The country {i} has been found at index {index}')

# for index, item in enumerate([20, 30, 40]):
#     print(index, item)

