
def show(article):
    print(article)

def show_list(site, titles):
    print(f'The latest tutorials from {site}')
    for article_id, title in enumerate(titles):
        print(f'{article_id:>3}{title}')

