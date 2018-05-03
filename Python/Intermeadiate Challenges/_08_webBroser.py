import webbrowser

sites = ['youtube', 'github', 'netflix']

for i in range(len(sites)):
    visit = 'https://{}.com/'.format(sites[i])
    webbrowser.open(visit)
