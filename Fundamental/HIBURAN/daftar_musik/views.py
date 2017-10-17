from models import musik

def view_musik():
    print('Daftar Musik')
    print('---')

    for m in musik:
        print(m)
