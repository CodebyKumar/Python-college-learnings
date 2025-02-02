from pathlib import Path
import zipfile
new_var=[]
def _walk(path:Path) -> new_var:
    all_files=[]
    for x in path.iterdir():
        if x.is_dir():
            all_files.extend(_walk(x))
        else:
            all_files.append(x)
    return all_files
        
def zip_files(path:Path,archive_name:str):
    all_files=_walk(path)
    with zipfile.ZipFile(f'{archive_name}','w',zipfile.ZIP_DEFLATED) as zipf:
        for f in all_files:
            zipf.write(f)
        zipf.close()

def zip_this_folder():
    print('compressing...')
    zip_files(Path.cwd(),'current_folder.zip')
    print(Path.cwd())
    print('...compression done!')


zip_this_folder()
