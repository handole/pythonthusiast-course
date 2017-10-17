from models import film

def view_film():
    print('Daftar Film')
    print('---')

    for f in film:
        print(f)