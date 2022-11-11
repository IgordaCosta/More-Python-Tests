import ccd2iso

Location = r'C:\Users\Dogman\Desktop\Saved Image Files\RaspberrypiQbit20220802' + '\\'

src_file = Location + 'RaspberrypiQbit20220802.img'

dst_file = Location + 'RaspberrypiQbit20220802.iso'

ccd2iso.convert(src_file= src_file, dst_file=dst_file, progress=True)