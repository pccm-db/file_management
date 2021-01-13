import os
import shutil


dir_path = os.path.join('mnt', 'd', 'WorkDocs', 'OneDrive', 'Prashanti_data_from_Documents', 'whatsapp_ot_dr_koppiker', '2020_12_22')
dir_path = '/mnt/d/WorkDocs/OneDrive/Prashanti_Data_from_Documents/whatsapp_ot_dr_koppiker/2020_12_22/'
with os.scandir(dir_path) as files:
    for file in files:
        filename = file.name
        if filename.endswith('.jpg'):
            loc_20 = filename.find('20')
            newdir = os.path.join('surgery_forms', filename[loc_20:(loc_20+10)])
            if not os.path.exists(newdir):
                os.mkdir(newdir)
            file = os.path.join(dir_path, filename)
            shutil.move(file, dst=newdir)
                
#todo: move files into the respective folders