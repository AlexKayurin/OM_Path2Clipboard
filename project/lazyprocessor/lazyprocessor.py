import sys
import os
import shutil
import subprocess

#  set paths
pathexport: str = r'C:\QINSy Project\Malta – Italy IC2\Export\TSS_Coils'
pathreport: str = r'Z:\03-Processing\02-Export\08-ID&C'
pathtrack: str = r'C:\Users\Public\tracks'
pathshape: str = r'C:\Users\Public\tracks shp'
tssscript: str = r'C:\Users\Public\TSS_TXT_TO_SHAPEFILE_conversion.ps1'

# target name
inptargetname = input('Check if filenames are correct and not duplicated\n Type targetname (like B01_MC01): ')
targetname: str = r'P2381_' + inptargetname

# copy 'TSS_coils' -> 'TARGET\TSS COILS' -> 'tracks' & rename
print('Copying coils files to Target Folder & renaming...')
filenames = next(os.walk(pathexport))[2]
for filename1 in filenames:
    for surveytype in ['AF', 'AL', ]:
        # check if 'targetname' in filename and not MBES file, copy to coil folder and rename
        if surveytype in filename1 and inptargetname in filename1 and 'MB' not in filename1:
            filename2 = filename1[5:].replace(' - 0001.filt', '')
            file1 = os.path.join(pathexport, filename1)
            file2 = os.path.join(pathreport, targetname, r'03-Hydropact440\04-TSS COILS', surveytype, filename2)
            try:
                shutil.copyfile(file1, file2)
            except FileNotFoundError:
                input('Check if target folder exists and repeat\n Press key to exit...')
                sys.exit(1)

            # copy to tracks folder and rename
            if 'CenterCoil' in  filename2:
                filename3 = filename2.replace('CenterCoil', 'TSS_TRACK')
                file3 = os.path.join(pathtrack, filename3)
                try:
                    shutil.copyfile(file2, file3)
                except FileNotFoundError:
                    print('Check if tracks folder exists and repeat\n Press key to exit...')
                    sys.exit(1)
print('OK')

# run TSS track PS script
print('Running Coils-to-Tracks script...')
p = subprocess.Popen(["powershell.exe", tssscript], stdout=sys.stdout)
p.communicate()
p.kill()
print('OK')


#  move tracks to target folder
print('Copying tracks files to Target Folder...')
filenames = next(os.walk(pathshape))[2]
for filename4 in filenames:
    for surveytype in ['AF', 'AL', ]:
        if surveytype in filename4:
            file4 = os.path.join(pathshape, filename4)
            file5 = os.path.join(pathreport, targetname, r'03-Hydropact440\01-TRACKS', surveytype, filename4)
            shutil.move(file4, file5)
print('OK')


# move original coils files to storage folder
filenames = next(os.walk(pathexport))[2]
pathstore = os.path.join(pathexport, inptargetname)
if not os.path.exists(pathstore):
    print('\tCreating storage folder...')
    os.mkdir(pathstore)
    print('\tOK')
else:
    print('\tPath already exists')

for filename5 in filenames:
    for surveytype in ['AF', 'AL', ]:
        if surveytype in filename5 and inptargetname in filename5 and 'MB' not in filename5:
            file6 = os.path.join(pathexport, filename5)
            file7 = os.path.join(pathstore, filename5)
            shutil.move(file6, file7)

print('OK')


input('\n\n\nCongratulations! You are the laziest Data Processor! Script has done your work.\n Press key to exit...')


