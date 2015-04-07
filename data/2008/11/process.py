from __future__ import with_statement
import os

urls = [
"pagecounts-20081101-000001",
"pagecounts-20081101-010000",
"pagecounts-20081101-020000",
"pagecounts-20081101-030000",
"pagecounts-20081101-040000",
"pagecounts-20081101-050001",
"pagecounts-20081101-060000",
"pagecounts-20081101-070000",
"pagecounts-20081101-080000",
"pagecounts-20081101-090000",
"pagecounts-20081101-100000",
"pagecounts-20081101-110000",
"pagecounts-20081101-120001",
"pagecounts-20081101-130000",
"pagecounts-20081101-140000",
"pagecounts-20081101-150000",
"pagecounts-20081101-160000",
"pagecounts-20081101-170001",
"pagecounts-20081101-180000",
"pagecounts-20081101-190000",
"pagecounts-20081101-200000",
"pagecounts-20081101-210000",
"pagecounts-20081101-220000",
"pagecounts-20081101-230000",
"pagecounts-20081102-000001",
"pagecounts-20081102-010000",
"pagecounts-20081102-020000",
"pagecounts-20081102-030000",
"pagecounts-20081102-040000",
"pagecounts-20081102-050000",
"pagecounts-20081102-060001",
"pagecounts-20081102-070000",
"pagecounts-20081102-080000",
"pagecounts-20081102-090000",
"pagecounts-20081102-100000",
"pagecounts-20081102-110000",
"pagecounts-20081102-120001",
"pagecounts-20081102-130000",
"pagecounts-20081102-140000",
"pagecounts-20081102-150000",
"pagecounts-20081102-160000",
"pagecounts-20081102-170000",
"pagecounts-20081102-180001",
"pagecounts-20081102-190000",
"pagecounts-20081102-200000",
"pagecounts-20081102-210000",
"pagecounts-20081102-220000",
"pagecounts-20081102-230000",
"pagecounts-20081103-000001",
"pagecounts-20081103-010000",
"pagecounts-20081103-020000",
"pagecounts-20081103-030000",
"pagecounts-20081103-040000",
"pagecounts-20081103-050000",
"pagecounts-20081103-060001",
"pagecounts-20081103-070000",
"pagecounts-20081103-080000",
"pagecounts-20081103-090000",
"pagecounts-20081103-100000",
"pagecounts-20081103-110000",
"pagecounts-20081103-120001",
"pagecounts-20081103-130000",
"pagecounts-20081103-140000",
"pagecounts-20081103-150000",
"pagecounts-20081103-160000",
"pagecounts-20081103-170000",
"pagecounts-20081103-180001",
"pagecounts-20081103-190000",
"pagecounts-20081103-200000",
"pagecounts-20081103-210000",
"pagecounts-20081103-220000",
"pagecounts-20081103-230000",
"pagecounts-20081104-000001",
"pagecounts-20081104-010000",
"pagecounts-20081104-020000",
"pagecounts-20081104-030000",
"pagecounts-20081104-040000",
"pagecounts-20081104-050000",
"pagecounts-20081104-060001",
"pagecounts-20081104-070000",
"pagecounts-20081104-080000",
"pagecounts-20081104-090000",
"pagecounts-20081104-100000",
"pagecounts-20081104-110000",
"pagecounts-20081104-120001",
"pagecounts-20081104-130000",
"pagecounts-20081104-140000",
"pagecounts-20081104-150000",
"pagecounts-20081104-160000",
"pagecounts-20081104-170000",
"pagecounts-20081104-180001",
"pagecounts-20081104-190000",
"pagecounts-20081104-200000",
"pagecounts-20081104-210000",
"pagecounts-20081104-220000",
"pagecounts-20081104-230000",
"pagecounts-20081105-000001",
"pagecounts-20081105-010000",
"pagecounts-20081105-020000",
"pagecounts-20081105-030000",
"pagecounts-20081105-040000",
"pagecounts-20081105-050001",
"pagecounts-20081105-060000",
"pagecounts-20081105-070000",
"pagecounts-20081105-080000",
"pagecounts-20081105-090000",
"pagecounts-20081105-100000",
"pagecounts-20081105-110001",
"pagecounts-20081105-120000",
"pagecounts-20081105-130000",
"pagecounts-20081105-140000",
"pagecounts-20081105-150000",
"pagecounts-20081105-160000",
"pagecounts-20081105-170001",
"pagecounts-20081105-180000",
"pagecounts-20081105-190000",
"pagecounts-20081105-200000",
"pagecounts-20081105-210000",
"pagecounts-20081105-220000",
"pagecounts-20081105-230000",
"pagecounts-20081106-000001",
"pagecounts-20081106-010000",
"pagecounts-20081106-020000",
"pagecounts-20081106-030000",
"pagecounts-20081106-040000",
"pagecounts-20081106-050001",
"pagecounts-20081106-060000",
"pagecounts-20081106-070000",
"pagecounts-20081106-080000",
"pagecounts-20081106-090000",
"pagecounts-20081106-100000",
"pagecounts-20081106-110001",
"pagecounts-20081106-120000",
"pagecounts-20081106-130000",
"pagecounts-20081106-140000",
"pagecounts-20081106-150000",
"pagecounts-20081106-160000",
"pagecounts-20081106-170001",
"pagecounts-20081106-180000",
"pagecounts-20081106-190000",
"pagecounts-20081106-200000",
"pagecounts-20081106-210000",
"pagecounts-20081106-220000",
"pagecounts-20081106-230001",
"pagecounts-20081107-000000",
"pagecounts-20081107-010000",
"pagecounts-20081107-020000",
"pagecounts-20081107-030000",
"pagecounts-20081107-040000",
"pagecounts-20081107-050001",
"pagecounts-20081107-060000",
"pagecounts-20081107-070000",
"pagecounts-20081107-080000",
"pagecounts-20081107-090000",
"pagecounts-20081107-100000",
"pagecounts-20081107-110001",
"pagecounts-20081107-120000",
"pagecounts-20081107-130000",
"pagecounts-20081107-140000",
"pagecounts-20081107-150000",
"pagecounts-20081107-160000",
"pagecounts-20081107-170000",
"pagecounts-20081107-180001",
"pagecounts-20081107-190000",
"pagecounts-20081107-200000",
"pagecounts-20081107-210000",
"pagecounts-20081107-220000",
"pagecounts-20081107-230000",
"pagecounts-20081108-000001",
"pagecounts-20081108-010000",
"pagecounts-20081108-020000",
"pagecounts-20081108-030000",
"pagecounts-20081108-040000",
"pagecounts-20081108-050000",
"pagecounts-20081108-060001",
"pagecounts-20081108-070000",
"pagecounts-20081108-080000",
"pagecounts-20081108-090000",
"pagecounts-20081108-100000",
"pagecounts-20081108-110001",
"pagecounts-20081108-120000",
"pagecounts-20081108-130000",
"pagecounts-20081108-140000",
"pagecounts-20081108-150000",
"pagecounts-20081108-160000",
"pagecounts-20081108-170000",
"pagecounts-20081108-180001",
"pagecounts-20081108-190000",
"pagecounts-20081108-200000",
"pagecounts-20081108-210000",
"pagecounts-20081108-220000",
"pagecounts-20081108-230001",
"pagecounts-20081109-000000",
"pagecounts-20081109-010000",
"pagecounts-20081109-020000",
"pagecounts-20081109-030000",
"pagecounts-20081109-040000",
"pagecounts-20081109-050001",
"pagecounts-20081109-060000",
"pagecounts-20081109-070000",
"pagecounts-20081109-080000",
"pagecounts-20081109-090000",
"pagecounts-20081109-100000",
"pagecounts-20081109-110001",
"pagecounts-20081109-120000",
"pagecounts-20081109-130000",
"pagecounts-20081109-140000",
"pagecounts-20081109-150000",
"pagecounts-20081109-160000",
"pagecounts-20081109-170001",
"pagecounts-20081109-180000",
"pagecounts-20081109-190000",
"pagecounts-20081109-200000",
"pagecounts-20081109-210000",
"pagecounts-20081109-220000",
"pagecounts-20081109-230001",
"pagecounts-20081110-000000",
"pagecounts-20081110-010000",
"pagecounts-20081110-020000",
"pagecounts-20081110-030000",
"pagecounts-20081110-040000",
"pagecounts-20081110-050001",
"pagecounts-20081110-060000",
"pagecounts-20081110-070000",
"pagecounts-20081110-080000",
"pagecounts-20081110-090000",
"pagecounts-20081110-100000",
"pagecounts-20081110-110001",
"pagecounts-20081110-120000",
"pagecounts-20081110-130000",
"pagecounts-20081110-140000",
"pagecounts-20081110-150000",
"pagecounts-20081110-160000",
"pagecounts-20081110-170001",
"pagecounts-20081110-180000",
"pagecounts-20081110-190000",
"pagecounts-20081110-200000",
"pagecounts-20081110-210000",
"pagecounts-20081110-220000",
"pagecounts-20081110-230001",
"pagecounts-20081111-000000",
"pagecounts-20081111-010000",
"pagecounts-20081111-020000",
"pagecounts-20081111-030000",
"pagecounts-20081111-040000",
"pagecounts-20081111-050001",
"pagecounts-20081111-060000",
"pagecounts-20081111-070000",
"pagecounts-20081111-080000",
"pagecounts-20081111-090000",
"pagecounts-20081111-100000",
"pagecounts-20081111-110001",
"pagecounts-20081111-120000",
"pagecounts-20081111-130000",
"pagecounts-20081111-140000",
"pagecounts-20081111-150000",
"pagecounts-20081111-160000",
"pagecounts-20081111-170000",
"pagecounts-20081111-180001",
"pagecounts-20081111-190000",
"pagecounts-20081111-200000",
"pagecounts-20081111-210000",
"pagecounts-20081111-220000",
"pagecounts-20081111-230000",
"pagecounts-20081112-000001",
"pagecounts-20081112-010000",
"pagecounts-20081112-020000",
"pagecounts-20081112-030000",
"pagecounts-20081112-040000",
"pagecounts-20081112-050000",
"pagecounts-20081112-060001",
"pagecounts-20081112-070000",
"pagecounts-20081112-080000",
"pagecounts-20081112-090000",
"pagecounts-20081112-100000",
"pagecounts-20081112-110000",
"pagecounts-20081112-120001",
"pagecounts-20081112-130000",
"pagecounts-20081112-140000",
"pagecounts-20081112-150000",
"pagecounts-20081112-160000",
"pagecounts-20081112-170000",
"pagecounts-20081112-180001",
"pagecounts-20081112-190000",
"pagecounts-20081112-200000",
"pagecounts-20081112-210000",
"pagecounts-20081112-220000",
"pagecounts-20081112-230000",
"pagecounts-20081113-000001",
"pagecounts-20081113-010000",
"pagecounts-20081113-020000",
"pagecounts-20081113-030000",
"pagecounts-20081113-040000",
"pagecounts-20081113-050000",
"pagecounts-20081113-060001",
"pagecounts-20081113-070000",
"pagecounts-20081113-080000",
"pagecounts-20081113-090000",
"pagecounts-20081113-100000",
"pagecounts-20081113-110000",
"pagecounts-20081113-120001",
"pagecounts-20081113-130000",
"pagecounts-20081113-140000",
"pagecounts-20081113-150000",
"pagecounts-20081113-160000",
"pagecounts-20081113-170000",
"pagecounts-20081113-180001",
"pagecounts-20081113-190000",
"pagecounts-20081113-200000",
"pagecounts-20081113-210000",
"pagecounts-20081113-220000",
"pagecounts-20081113-230000",
"pagecounts-20081114-000001",
"pagecounts-20081114-010000",
"pagecounts-20081114-020000",
"pagecounts-20081114-030000",
"pagecounts-20081114-040000",
"pagecounts-20081114-050000",
"pagecounts-20081114-060001",
"pagecounts-20081114-070000",
"pagecounts-20081114-080000",
"pagecounts-20081114-090000",
"pagecounts-20081114-100000",
"pagecounts-20081114-110001",
"pagecounts-20081114-120000",
"pagecounts-20081114-130000",
"pagecounts-20081114-140000",
"pagecounts-20081114-150000",
"pagecounts-20081114-160000",
"pagecounts-20081114-170001",
"pagecounts-20081114-180000",
"pagecounts-20081114-190000",
"pagecounts-20081114-200000",
"pagecounts-20081114-210000",
"pagecounts-20081114-220000",
"pagecounts-20081114-230001",
"pagecounts-20081115-000000",
"pagecounts-20081115-010000",
"pagecounts-20081115-020000",
"pagecounts-20081115-030000",
"pagecounts-20081115-040000",
"pagecounts-20081115-050001",
"pagecounts-20081115-060000",
"pagecounts-20081115-070000",
"pagecounts-20081115-080000",
"pagecounts-20081115-090000",
"pagecounts-20081115-100000",
"pagecounts-20081115-110001",
"pagecounts-20081115-120000",
"pagecounts-20081115-130000",
"pagecounts-20081115-140000",
"pagecounts-20081115-150000",
"pagecounts-20081115-160000",
"pagecounts-20081115-170001",
"pagecounts-20081115-180000",
"pagecounts-20081115-190000",
"pagecounts-20081115-200000",
"pagecounts-20081115-210000",
"pagecounts-20081115-220000",
"pagecounts-20081115-230001",
"pagecounts-20081116-000000",
"pagecounts-20081116-010000",
"pagecounts-20081116-020000",
"pagecounts-20081116-030000",
"pagecounts-20081116-040000",
"pagecounts-20081116-050001",
"pagecounts-20081116-060000",
"pagecounts-20081116-070000",
"pagecounts-20081116-080000",
"pagecounts-20081116-090000",
"pagecounts-20081116-100000",
"pagecounts-20081116-110001",
"pagecounts-20081116-120000",
"pagecounts-20081116-130000",
"pagecounts-20081116-140000",
"pagecounts-20081116-150000",
"pagecounts-20081116-160000",
"pagecounts-20081116-170001",
"pagecounts-20081116-180000",
"pagecounts-20081116-190000",
"pagecounts-20081116-200000",
"pagecounts-20081116-210000",
"pagecounts-20081116-220000",
"pagecounts-20081116-230001",
"pagecounts-20081117-000000",
"pagecounts-20081117-010000",
"pagecounts-20081117-020000",
"pagecounts-20081117-030000",
"pagecounts-20081117-040000",
"pagecounts-20081117-050001",
"pagecounts-20081117-060000",
"pagecounts-20081117-070000",
"pagecounts-20081117-080000",
"pagecounts-20081117-090000",
"pagecounts-20081117-100000",
"pagecounts-20081117-110001",
"pagecounts-20081117-120000",
"pagecounts-20081117-130000",
"pagecounts-20081117-140000",
"pagecounts-20081117-150000",
"pagecounts-20081117-160000",
"pagecounts-20081117-170001",
"pagecounts-20081117-180000",
"pagecounts-20081117-190000",
"pagecounts-20081117-200000",
"pagecounts-20081117-210000",
"pagecounts-20081117-220000",
"pagecounts-20081117-230001",
"pagecounts-20081118-000000",
"pagecounts-20081118-010000",
"pagecounts-20081118-020000",
"pagecounts-20081118-030000",
"pagecounts-20081118-040000",
"pagecounts-20081118-050001",
"pagecounts-20081118-060000",
"pagecounts-20081118-070000",
"pagecounts-20081118-080000",
"pagecounts-20081118-090000",
"pagecounts-20081118-100000",
"pagecounts-20081118-110000",
"pagecounts-20081118-120001",
"pagecounts-20081118-130000",
"pagecounts-20081118-140000",
"pagecounts-20081118-150000",
"pagecounts-20081118-160000",
"pagecounts-20081118-170001",
"pagecounts-20081118-180000",
"pagecounts-20081118-190000",
"pagecounts-20081118-200000",
"pagecounts-20081118-210000",
"pagecounts-20081118-220000",
"pagecounts-20081118-230001",
"pagecounts-20081119-000000",
"pagecounts-20081119-010000",
"pagecounts-20081119-020000",
"pagecounts-20081119-030000",
"pagecounts-20081119-040000",
"pagecounts-20081119-050000",
"pagecounts-20081119-060001",
"pagecounts-20081119-070000",
"pagecounts-20081119-080000",
"pagecounts-20081119-090000",
"pagecounts-20081119-100000",
"pagecounts-20081119-110001",
"pagecounts-20081119-120000",
"pagecounts-20081119-130000",
"pagecounts-20081119-140000",
"pagecounts-20081119-150000",
"pagecounts-20081119-160000",
"pagecounts-20081119-170001",
"pagecounts-20081119-180000",
"pagecounts-20081119-190000",
"pagecounts-20081119-200000",
"pagecounts-20081119-210000",
"pagecounts-20081119-220000",
"pagecounts-20081119-230000",
"pagecounts-20081120-000001",
"pagecounts-20081120-010000",
"pagecounts-20081120-020000",
"pagecounts-20081120-030000",
"pagecounts-20081120-040000",
"pagecounts-20081120-050000",
"pagecounts-20081120-060001",
"pagecounts-20081120-070000",
"pagecounts-20081120-080000",
"pagecounts-20081120-090000",
"pagecounts-20081120-100000",
"pagecounts-20081120-110000",
"pagecounts-20081120-120001",
"pagecounts-20081120-130000",
"pagecounts-20081120-140000",
"pagecounts-20081120-150000",
"pagecounts-20081120-160000",
"pagecounts-20081120-170000",
"pagecounts-20081120-180001",
"pagecounts-20081120-190000",
"pagecounts-20081120-200000",
"pagecounts-20081120-210000",
"pagecounts-20081120-220000",
"pagecounts-20081120-230000",
"pagecounts-20081121-000001",
"pagecounts-20081121-010000",
"pagecounts-20081121-020000",
"pagecounts-20081121-030000",
"pagecounts-20081121-040000",
"pagecounts-20081121-050001",
"pagecounts-20081121-060000",
"pagecounts-20081121-070000",
"pagecounts-20081121-080000",
"pagecounts-20081121-090000",
"pagecounts-20081121-100000",
"pagecounts-20081121-110001",
"pagecounts-20081121-120000",
"pagecounts-20081121-130000",
"pagecounts-20081121-140000",
"pagecounts-20081121-150000",
"pagecounts-20081121-160000",
"pagecounts-20081121-170001",
"pagecounts-20081121-180000",
"pagecounts-20081121-190000",
"pagecounts-20081121-200000",
"pagecounts-20081121-210000",
"pagecounts-20081121-220000",
"pagecounts-20081121-230000",
"pagecounts-20081122-000001",
"pagecounts-20081122-010000",
"pagecounts-20081122-020000",
"pagecounts-20081122-030000",
"pagecounts-20081122-040000",
"pagecounts-20081122-050000",
"pagecounts-20081122-060001",
"pagecounts-20081122-070000",
"pagecounts-20081122-080000",
"pagecounts-20081122-090000",
"pagecounts-20081122-100000",
"pagecounts-20081122-110000",
"pagecounts-20081122-120001",
"pagecounts-20081122-130000",
"pagecounts-20081122-140000",
"pagecounts-20081122-150000",
"pagecounts-20081122-160000",
"pagecounts-20081122-170000",
"pagecounts-20081122-180001",
"pagecounts-20081122-190000",
"pagecounts-20081122-200000",
"pagecounts-20081122-210000",
"pagecounts-20081122-220000",
"pagecounts-20081122-230000",
"pagecounts-20081123-000001",
"pagecounts-20081123-010000",
"pagecounts-20081123-020000",
"pagecounts-20081123-030000",
"pagecounts-20081123-040000",
"pagecounts-20081123-050000",
"pagecounts-20081123-060001",
"pagecounts-20081123-070000",
"pagecounts-20081123-080000",
"pagecounts-20081123-090000",
"pagecounts-20081123-100000",
"pagecounts-20081123-110000",
"pagecounts-20081123-120001",
"pagecounts-20081123-130000",
"pagecounts-20081123-140000",
"pagecounts-20081123-150000",
"pagecounts-20081123-160000",
"pagecounts-20081123-170000",
"pagecounts-20081123-180001",
"pagecounts-20081123-190000",
"pagecounts-20081123-200000",
"pagecounts-20081123-210000",
"pagecounts-20081123-220000",
"pagecounts-20081123-230000",
"pagecounts-20081124-000001",
"pagecounts-20081124-010000",
"pagecounts-20081124-020000",
"pagecounts-20081124-030000",
"pagecounts-20081124-040000",
"pagecounts-20081124-050000",
"pagecounts-20081124-060001",
"pagecounts-20081124-070000",
"pagecounts-20081124-080000",
"pagecounts-20081124-090000",
"pagecounts-20081124-100000",
"pagecounts-20081124-110000",
"pagecounts-20081124-120001",
"pagecounts-20081124-130000",
"pagecounts-20081124-140000",
"pagecounts-20081124-150000",
"pagecounts-20081124-160000",
"pagecounts-20081124-170000",
"pagecounts-20081124-180001",
"pagecounts-20081124-190000",
"pagecounts-20081124-200000",
"pagecounts-20081124-210000",
"pagecounts-20081124-220000",
"pagecounts-20081124-230000",
"pagecounts-20081125-000001",
"pagecounts-20081125-010000",
"pagecounts-20081125-020000",
"pagecounts-20081125-030000",
"pagecounts-20081125-040000",
"pagecounts-20081125-050000",
"pagecounts-20081125-060001",
"pagecounts-20081125-070000",
"pagecounts-20081125-080000",
"pagecounts-20081125-090000",
"pagecounts-20081125-100000",
"pagecounts-20081125-110000",
"pagecounts-20081125-120001",
"pagecounts-20081125-130000",
"pagecounts-20081125-140000",
"pagecounts-20081125-150000",
"pagecounts-20081125-160000",
"pagecounts-20081125-170000",
"pagecounts-20081125-180001",
"pagecounts-20081125-190000",
"pagecounts-20081125-200000",
"pagecounts-20081125-210000",
"pagecounts-20081125-220000",
"pagecounts-20081125-230000",
"pagecounts-20081126-000001",
"pagecounts-20081126-010000",
"pagecounts-20081126-020000",
"pagecounts-20081126-030000",
"pagecounts-20081126-040000",
"pagecounts-20081126-050000",
"pagecounts-20081126-060001",
"pagecounts-20081126-070000",
"pagecounts-20081126-080000",
"pagecounts-20081126-090000",
"pagecounts-20081126-100000",
"pagecounts-20081126-110000",
"pagecounts-20081126-120001",
"pagecounts-20081126-130000",
"pagecounts-20081126-140000",
"pagecounts-20081126-150000",
"pagecounts-20081126-160000",
"pagecounts-20081126-170000",
"pagecounts-20081126-180001",
"pagecounts-20081126-190000",
"pagecounts-20081126-200000",
"pagecounts-20081126-210000",
"pagecounts-20081126-220000",
"pagecounts-20081126-230000",
"pagecounts-20081127-000001",
"pagecounts-20081127-010000",
"pagecounts-20081127-020000",
"pagecounts-20081127-030000",
"pagecounts-20081127-040000",
"pagecounts-20081127-050000",
"pagecounts-20081127-060001",
"pagecounts-20081127-070000",
"pagecounts-20081127-080000",
"pagecounts-20081127-090000",
"pagecounts-20081127-100000",
"pagecounts-20081127-110000",
"pagecounts-20081127-120001",
"pagecounts-20081127-130000",
"pagecounts-20081127-140000",
"pagecounts-20081127-150000",
"pagecounts-20081127-160000",
"pagecounts-20081127-170000",
"pagecounts-20081127-180001",
"pagecounts-20081127-190000",
"pagecounts-20081127-200000",
"pagecounts-20081127-210000",
"pagecounts-20081127-220000",
"pagecounts-20081127-230000",
"pagecounts-20081128-000000",
"pagecounts-20081128-010001",
"pagecounts-20081128-020000",
"pagecounts-20081128-030000",
"pagecounts-20081128-040000",
"pagecounts-20081128-050000",
"pagecounts-20081128-060000",
"pagecounts-20081128-070001",
"pagecounts-20081128-080000",
"pagecounts-20081128-090000",
"pagecounts-20081128-100000",
"pagecounts-20081128-110000",
"pagecounts-20081128-120000",
"pagecounts-20081128-130001",
"pagecounts-20081128-140000",
"pagecounts-20081128-150000",
"pagecounts-20081128-160000",
"pagecounts-20081128-170000",
"pagecounts-20081128-180000",
"pagecounts-20081128-190001",
"pagecounts-20081128-200000",
"pagecounts-20081128-210000",
"pagecounts-20081128-220000",
"pagecounts-20081128-230000",
"pagecounts-20081129-000000",
"pagecounts-20081129-010001",
"pagecounts-20081129-020000",
"pagecounts-20081129-030000",
"pagecounts-20081129-040000",
"pagecounts-20081129-050000",
"pagecounts-20081129-060000",
"pagecounts-20081129-070001",
"pagecounts-20081129-080000",
"pagecounts-20081129-090000",
"pagecounts-20081129-100000",
"pagecounts-20081129-110000",
"pagecounts-20081129-120000",
"pagecounts-20081129-130001",
"pagecounts-20081129-140000",
"pagecounts-20081129-150000",
"pagecounts-20081129-160000",
"pagecounts-20081129-170000",
"pagecounts-20081129-180000",
"pagecounts-20081129-190001",
"pagecounts-20081129-200000",
"pagecounts-20081129-210000",
"pagecounts-20081129-220000",
"pagecounts-20081129-230000",
"pagecounts-20081130-000000",
"pagecounts-20081130-010000",
"pagecounts-20081130-020001",
"pagecounts-20081130-030000",
"pagecounts-20081130-040000",
"pagecounts-20081130-050000",
"pagecounts-20081130-060000",
"pagecounts-20081130-070001",
"pagecounts-20081130-080000",
"pagecounts-20081130-090000",
"pagecounts-20081130-100000",
"pagecounts-20081130-110000",
"pagecounts-20081130-120000",
"pagecounts-20081130-130001",
"pagecounts-20081130-140000",
"pagecounts-20081130-150000",
"pagecounts-20081130-160000",
"pagecounts-20081130-170000",
"pagecounts-20081130-180000",
"pagecounts-20081130-190001",
"pagecounts-20081130-200000",
"pagecounts-20081130-210000",
"pagecounts-20081130-220000",
"pagecounts-20081130-230000",
]

base = "http://dumps.wikimedia.org/other/pagecounts-raw/"
tail = "2008/2008-11/"

print "Unzipping..."
os.system("gunzip *.gz")

i = 0
for url in urls:
  if not os.path.isfile("en-" + url):
    f_size = os.stat(url).st_size
    if not os.path.isfile(url) or f_size < 100L:
      os.system("rm " + url)
      os.system("curl -O %s.gz" % (base + tail + url))
      os.system("gunzip " + url + ".gz")

    with open(url, "r") as full:
      new = open("en-" + url, "w")
      for line in full:
        if line[0:2] == "en":
          new.write(line)
      new.close()
  i = i + 1
  print "%d of %d complete" % (i, len(urls))
  if os.path.isfile(url):
    os.system("rm " + url)
  if os.stat("en-" + url).st_size < 100L:
    print url
