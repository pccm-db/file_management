files = ["00000144-PHOTO-2019-07-27-17-29-48.jpg",          # please dont hard code information. Either created and read a txt/csv file or in this case you need to use package
              "00000145-PHOTO-2019-07-27-17-29-53.jpg",     # OS to get folder information
              "00000146-PHOTO-2019-07-27-17-30-04.jpg",
              "00000147-PHOTO-2019-07-27-17-30-12.jpg",
              "00000148-PHOTO-2019-07-27-17-30-14.jpg",
              "00000149-PHOTO-2019-07-27-17-30-15.jpg",
              "00000230-JH - Dr. Aavantika Bhat.vcf"
    ]

###############################################################
substring = "PHOTO"

jpg_image_name = []                                         # please see scan rename files for an example of how I have done this.
not_jpg_image_name = []



for file in files:
    if file.endswith('.jpg'):
        loc = file.find(substring)
        dt = file[loc]
    else:
        not_jpg_image_name.append(string)
        
##################################################################
unnecessary_words = ['PHOTO',".jpg"]

# for i in unnecessary_words:
#     for string in jpg_image_name:
#         string = string.replace(i, '') 
  
      
        
 
    
