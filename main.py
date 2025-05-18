import os, sys, shutil, zipfile

here = os.getcwd()
contest_dir = os.path.join(here, 'contest')
des_path = os.path.join(contest_dir, 'quera-format')

items = os.listdir(contest_dir)
if 'paste-here' in items:
    items.remove('paste-here')
if 'quera-format' in items:
    shutil.rmtree(des_path)
    items.remove('quera-format')
    

if len(items) != 1:
    print('Error: You should only keep your contest folder in the contest folder. If you have any extra items, delete them or add them if you don\'t have them.')
    sys.exit(1)
    
contest_name = items[0]
contest_name_dir = os.path.join(contest_dir, contest_name)

os.makedirs(des_path, exist_ok=True) # make quera-format folder again

problem_number = 0
hoj_problems = os.listdir(contest_name_dir)
for hoj_problem in sorted(hoj_problems):
    if hoj_problem.endswith('.zip'):
        quera_problem_dir = os.path.join(des_path, chr(ord('A') + problem_number))
        os.makedirs(quera_problem_dir)
        problem_number += 1
        
        in_folder = os.path.join(quera_problem_dir, 'in')
        out_folder = os.path.join(quera_problem_dir, 'out')
        os.makedirs(in_folder)
        os.makedirs(out_folder)
        
        original_zip_path = os.path.join(contest_name_dir, hoj_problem)
        with zipfile.ZipFile(original_zip_path, 'r') as original_zip:
            for file_name in original_zip.namelist():
                if file_name.endswith('.in'):
                    test_case_num = file_name[:-3] # removing .in
                    new_file_name = f'input{test_case_num}.txt'
                    new_file_path = os.path.join(in_folder, new_file_name)
                elif file_name.endswith('.out'):
                    test_case_num = file_name[:-4] # removing .out
                    new_file_name = f'output{test_case_num}.txt'
                    new_file_path = os.path.join(out_folder, new_file_name)
                else:
                    continue # ignore other files
            
                with original_zip.open(file_name) as source_file:
                    with open(new_file_path, 'wb') as dest_file:
                        dest_file.write(source_file.read())
        
        # create new zip file
        new_zip_path = os.path.join(quera_problem_dir, 'problem.zip')
        with zipfile.ZipFile(new_zip_path, 'w') as new_zip:
            for folder in ['in', 'out']:
                for root, _, files in os.walk(os.path.join(quera_problem_dir, folder)):
                    for file in files:
                        file_path = os.path.join(root, file)
                        new_zip.write(file_path, os.path.join(*os.path.relpath(file_path, new_zip_path).split('/')[1:]))

        shutil.rmtree(in_folder)
        shutil.rmtree(out_folder)

print('converted successfully, You can see the converted formatted samples in the ./quera-format folder.')