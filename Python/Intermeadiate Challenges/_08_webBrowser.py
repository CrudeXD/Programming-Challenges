import webbrowser

sites = ['youtube', 'github']

for i in range(len(sites)):
    visit = 'https://{}.com/'.format(sites[i])
    webbrowser.open(visit)
