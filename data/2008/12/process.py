from __future__ import with_statement
import os

urls = [
"pagecounts-20081201-000000",
"pagecounts-20081201-010001",
"pagecounts-20081201-020000",
"pagecounts-20081201-030000",
"pagecounts-20081201-040000",
"pagecounts-20081201-050000",
"pagecounts-20081201-060000",
"pagecounts-20081201-070001",
"pagecounts-20081201-080000",
"pagecounts-20081201-090000",
"pagecounts-20081201-100000",
"pagecounts-20081201-110000",
"pagecounts-20081201-120000",
"pagecounts-20081201-130000",
"pagecounts-20081201-140001",
"pagecounts-20081201-150000",
"pagecounts-20081201-160000",
"pagecounts-20081201-170000",
"pagecounts-20081201-180000",
"pagecounts-20081201-190000",
"pagecounts-20081201-200001",
"pagecounts-20081201-210000",
"pagecounts-20081201-220000",
"pagecounts-20081201-230000",
"pagecounts-20081202-000000",
"pagecounts-20081202-010000",
"pagecounts-20081202-020001",
"pagecounts-20081202-030000",
"pagecounts-20081202-040000",
"pagecounts-20081202-050000",
"pagecounts-20081202-060000",
"pagecounts-20081202-070000",
"pagecounts-20081202-080001",
"pagecounts-20081202-090000",
"pagecounts-20081202-100000",
"pagecounts-20081202-110000",
"pagecounts-20081202-120000",
"pagecounts-20081202-130001",
"pagecounts-20081202-140000",
"pagecounts-20081202-150000",
"pagecounts-20081202-160000",
"pagecounts-20081202-170000",
"pagecounts-20081202-180000",
"pagecounts-20081202-190000",
"pagecounts-20081202-200001",
"pagecounts-20081202-210000",
"pagecounts-20081202-220000",
"pagecounts-20081202-230000",
"pagecounts-20081203-000000",
"pagecounts-20081203-010000",
"pagecounts-20081203-020001",
"pagecounts-20081203-030000",
"pagecounts-20081203-040000",
"pagecounts-20081203-050000",
"pagecounts-20081203-060000",
"pagecounts-20081203-070000",
"pagecounts-20081203-080001",
"pagecounts-20081203-090000",
"pagecounts-20081203-100000",
"pagecounts-20081203-110000",
"pagecounts-20081203-120000",
"pagecounts-20081203-130001",
"pagecounts-20081203-140000",
"pagecounts-20081203-150000",
"pagecounts-20081203-160000",
"pagecounts-20081203-170000",
"pagecounts-20081203-180000",
"pagecounts-20081203-190000",
"pagecounts-20081203-200001",
"pagecounts-20081203-210000",
"pagecounts-20081203-220000",
"pagecounts-20081203-230000",
"pagecounts-20081204-000000",
"pagecounts-20081204-010000",
"pagecounts-20081204-020001",
"pagecounts-20081204-030000",
"pagecounts-20081204-040000",
"pagecounts-20081204-050000",
"pagecounts-20081204-060000",
"pagecounts-20081204-070000",
"pagecounts-20081204-080001",
"pagecounts-20081204-090000",
"pagecounts-20081204-100000",
"pagecounts-20081204-110000",
"pagecounts-20081204-120000",
"pagecounts-20081204-130000",
"pagecounts-20081204-140001",
"pagecounts-20081204-150000",
"pagecounts-20081204-160000",
"pagecounts-20081204-170000",
"pagecounts-20081204-180000",
"pagecounts-20081204-190000",
"pagecounts-20081204-200001",
"pagecounts-20081204-210000",
"pagecounts-20081204-220000",
"pagecounts-20081204-230000",
"pagecounts-20081205-000000",
"pagecounts-20081205-010000",
"pagecounts-20081205-020001",
"pagecounts-20081205-030000",
"pagecounts-20081205-040000",
"pagecounts-20081205-050000",
"pagecounts-20081205-060000",
"pagecounts-20081205-070000",
"pagecounts-20081205-080001",
"pagecounts-20081205-090000",
"pagecounts-20081205-100000",
"pagecounts-20081205-110000",
"pagecounts-20081205-120000",
"pagecounts-20081205-130000",
"pagecounts-20081205-140001",
"pagecounts-20081205-150000",
"pagecounts-20081205-160000",
"pagecounts-20081205-170000",
"pagecounts-20081205-180000",
"pagecounts-20081205-190000",
"pagecounts-20081205-200001",
"pagecounts-20081205-210000",
"pagecounts-20081205-220000",
"pagecounts-20081205-230000",
"pagecounts-20081206-000000",
"pagecounts-20081206-010000",
"pagecounts-20081206-020000",
"pagecounts-20081206-030001",
"pagecounts-20081206-040000",
"pagecounts-20081206-050000",
"pagecounts-20081206-060000",
"pagecounts-20081206-070000",
"pagecounts-20081206-080000",
"pagecounts-20081206-090001",
"pagecounts-20081206-100000",
"pagecounts-20081206-110000",
"pagecounts-20081206-120000",
"pagecounts-20081206-130000",
"pagecounts-20081206-140000",
"pagecounts-20081206-150001",
"pagecounts-20081206-160000",
"pagecounts-20081206-170000",
"pagecounts-20081206-180000",
"pagecounts-20081206-190000",
"pagecounts-20081206-200000",
"pagecounts-20081206-210001",
"pagecounts-20081206-220000",
"pagecounts-20081206-230000",
"pagecounts-20081207-000000",
"pagecounts-20081207-010000",
"pagecounts-20081207-020000",
"pagecounts-20081207-030001",
"pagecounts-20081207-040000",
"pagecounts-20081207-050000",
"pagecounts-20081207-060000",
"pagecounts-20081207-070000",
"pagecounts-20081207-080000",
"pagecounts-20081207-090001",
"pagecounts-20081207-100000",
"pagecounts-20081207-110000",
"pagecounts-20081207-120000",
"pagecounts-20081207-130000",
"pagecounts-20081207-140000",
"pagecounts-20081207-150000",
"pagecounts-20081207-160001",
"pagecounts-20081207-170000",
"pagecounts-20081207-180000",
"pagecounts-20081207-190000",
"pagecounts-20081207-200000",
"pagecounts-20081207-210000",
"pagecounts-20081207-220001",
"pagecounts-20081207-230000",
"pagecounts-20081208-000000",
"pagecounts-20081208-010000",
"pagecounts-20081208-020000",
"pagecounts-20081208-030000",
"pagecounts-20081208-040001",
"pagecounts-20081208-050000",
"pagecounts-20081208-060000",
"pagecounts-20081208-070000",
"pagecounts-20081208-080000",
"pagecounts-20081208-090000",
"pagecounts-20081208-100001",
"pagecounts-20081208-110000",
"pagecounts-20081208-120000",
"pagecounts-20081208-130000",
"pagecounts-20081208-140000",
"pagecounts-20081208-150000",
"pagecounts-20081208-160001",
"pagecounts-20081208-170000",
"pagecounts-20081208-180000",
"pagecounts-20081208-190000",
"pagecounts-20081208-200000",
"pagecounts-20081208-210000",
"pagecounts-20081208-220001",
"pagecounts-20081208-230000",
"pagecounts-20081209-000000",
"pagecounts-20081209-010000",
"pagecounts-20081209-020000",
"pagecounts-20081209-030000",
"pagecounts-20081209-040001",
"pagecounts-20081209-050000",
"pagecounts-20081209-060000",
"pagecounts-20081209-070000",
"pagecounts-20081209-080000",
"pagecounts-20081209-090000",
"pagecounts-20081209-100000",
"pagecounts-20081209-110001",
"pagecounts-20081209-120000",
"pagecounts-20081209-130000",
"pagecounts-20081209-140000",
"pagecounts-20081209-150000",
"pagecounts-20081209-160000",
"pagecounts-20081209-170001",
"pagecounts-20081209-180000",
"pagecounts-20081209-190000",
"pagecounts-20081209-200000",
"pagecounts-20081209-210000",
"pagecounts-20081209-220000",
"pagecounts-20081209-230001",
"pagecounts-20081210-000000",
"pagecounts-20081210-010000",
"pagecounts-20081210-020000",
"pagecounts-20081210-030000",
"pagecounts-20081210-040000",
"pagecounts-20081210-050001",
"pagecounts-20081210-060000",
"pagecounts-20081210-070000",
"pagecounts-20081210-080000",
"pagecounts-20081210-090000",
"pagecounts-20081210-100000",
"pagecounts-20081210-110001",
"pagecounts-20081210-120000",
"pagecounts-20081210-130000",
"pagecounts-20081210-140000",
"pagecounts-20081210-150000",
"pagecounts-20081210-160000",
"pagecounts-20081210-170001",
"pagecounts-20081210-180000",
"pagecounts-20081210-190000",
"pagecounts-20081210-200000",
"pagecounts-20081210-210000",
"pagecounts-20081210-220000",
"pagecounts-20081210-230001",
"pagecounts-20081211-000000",
"pagecounts-20081211-010000",
"pagecounts-20081211-020000",
"pagecounts-20081211-030000",
"pagecounts-20081211-040000",
"pagecounts-20081211-050001",
"pagecounts-20081211-060000",
"pagecounts-20081211-070000",
"pagecounts-20081211-080000",
"pagecounts-20081211-090000",
"pagecounts-20081211-100000",
"pagecounts-20081211-110001",
"pagecounts-20081211-120000",
"pagecounts-20081211-130000",
"pagecounts-20081211-140000",
"pagecounts-20081211-150000",
"pagecounts-20081211-160000",
"pagecounts-20081211-170001",
"pagecounts-20081211-180000",
"pagecounts-20081211-190000",
"pagecounts-20081211-200000",
"pagecounts-20081211-210000",
"pagecounts-20081211-220000",
"pagecounts-20081211-230001",
"pagecounts-20081212-000000",
"pagecounts-20081212-010000",
"pagecounts-20081212-020000",
"pagecounts-20081212-030000",
"pagecounts-20081212-040000",
"pagecounts-20081212-050000",
"pagecounts-20081212-060001",
"pagecounts-20081212-070000",
"pagecounts-20081212-080000",
"pagecounts-20081212-090000",
"pagecounts-20081212-100000",
"pagecounts-20081212-110000",
"pagecounts-20081212-120001",
"pagecounts-20081212-130000",
"pagecounts-20081212-140000",
"pagecounts-20081212-150000",
"pagecounts-20081212-160000",
"pagecounts-20081212-170000",
"pagecounts-20081212-180001",
"pagecounts-20081212-190000",
"pagecounts-20081212-200000",
"pagecounts-20081212-210000",
"pagecounts-20081212-220000",
"pagecounts-20081212-230000",
"pagecounts-20081213-000001",
"pagecounts-20081213-010000",
"pagecounts-20081213-020000",
"pagecounts-20081213-030000",
"pagecounts-20081213-040000",
"pagecounts-20081213-050000",
"pagecounts-20081213-060001",
"pagecounts-20081213-070000",
"pagecounts-20081213-080000",
"pagecounts-20081213-090000",
"pagecounts-20081213-100000",
"pagecounts-20081213-110000",
"pagecounts-20081213-120001",
"pagecounts-20081213-130000",
"pagecounts-20081213-140000",
"pagecounts-20081213-150000",
"pagecounts-20081213-160000",
"pagecounts-20081213-170000",
"pagecounts-20081213-180001",
"pagecounts-20081213-190000",
"pagecounts-20081213-200000",
"pagecounts-20081213-210000",
"pagecounts-20081213-220000",
"pagecounts-20081213-230000",
"pagecounts-20081214-000001",
"pagecounts-20081214-010000",
"pagecounts-20081214-020000",
"pagecounts-20081214-030000",
"pagecounts-20081214-040000",
"pagecounts-20081214-050000",
"pagecounts-20081214-060001",
"pagecounts-20081214-070000",
"pagecounts-20081214-080000",
"pagecounts-20081214-090000",
"pagecounts-20081214-100000",
"pagecounts-20081214-110000",
"pagecounts-20081214-120001",
"pagecounts-20081214-130000",
"pagecounts-20081214-140000",
"pagecounts-20081214-150000",
"pagecounts-20081214-160000",
"pagecounts-20081214-170000",
"pagecounts-20081214-180001",
"pagecounts-20081214-190000",
"pagecounts-20081214-200000",
"pagecounts-20081214-210000",
"pagecounts-20081214-220000",
"pagecounts-20081214-230000",
"pagecounts-20081215-000001",
"pagecounts-20081215-010000",
"pagecounts-20081215-020000",
"pagecounts-20081215-030000",
"pagecounts-20081215-040000",
"pagecounts-20081215-050000",
"pagecounts-20081215-060001",
"pagecounts-20081215-070000",
"pagecounts-20081215-080000",
"pagecounts-20081215-090000",
"pagecounts-20081215-100000",
"pagecounts-20081215-110000",
"pagecounts-20081215-120001",
"pagecounts-20081215-130000",
"pagecounts-20081215-140000",
"pagecounts-20081215-150000",
"pagecounts-20081215-160000",
"pagecounts-20081215-170000",
"pagecounts-20081215-180001",
"pagecounts-20081215-190000",
"pagecounts-20081215-200000",
"pagecounts-20081215-210000",
"pagecounts-20081215-220000",
"pagecounts-20081215-230000",
"pagecounts-20081216-000001",
"pagecounts-20081216-010000",
"pagecounts-20081216-020000",
"pagecounts-20081216-030000",
"pagecounts-20081216-040000",
"pagecounts-20081216-050000",
"pagecounts-20081216-060001",
"pagecounts-20081216-070000",
"pagecounts-20081216-080000",
"pagecounts-20081216-090000",
"pagecounts-20081216-100000",
"pagecounts-20081216-110000",
"pagecounts-20081216-120001",
"pagecounts-20081216-130000",
"pagecounts-20081216-140000",
"pagecounts-20081216-150000",
"pagecounts-20081216-160000",
"pagecounts-20081216-170000",
"pagecounts-20081216-180001",
"pagecounts-20081216-190000",
"pagecounts-20081216-200000",
"pagecounts-20081216-210000",
"pagecounts-20081216-220000",
"pagecounts-20081216-230000",
"pagecounts-20081217-000001",
"pagecounts-20081217-010000",
"pagecounts-20081217-020000",
"pagecounts-20081217-030000",
"pagecounts-20081217-040000",
"pagecounts-20081217-050000",
"pagecounts-20081217-060001",
"pagecounts-20081217-070000",
"pagecounts-20081217-080000",
"pagecounts-20081217-090000",
"pagecounts-20081217-100000",
"pagecounts-20081217-110000",
"pagecounts-20081217-120001",
"pagecounts-20081217-130000",
"pagecounts-20081217-140000",
"pagecounts-20081217-150000",
"pagecounts-20081217-160000",
"pagecounts-20081217-170000",
"pagecounts-20081217-180001",
"pagecounts-20081217-190000",
"pagecounts-20081217-200000",
"pagecounts-20081217-210000",
"pagecounts-20081217-220000",
"pagecounts-20081217-230000",
"pagecounts-20081218-000001",
"pagecounts-20081218-010000",
"pagecounts-20081218-020000",
"pagecounts-20081218-030000",
"pagecounts-20081218-040000",
"pagecounts-20081218-050000",
"pagecounts-20081218-060001",
"pagecounts-20081218-070000",
"pagecounts-20081218-080000",
"pagecounts-20081218-090000",
"pagecounts-20081218-100000",
"pagecounts-20081218-110000",
"pagecounts-20081218-120000",
"pagecounts-20081218-130001",
"pagecounts-20081218-140000",
"pagecounts-20081218-150000",
"pagecounts-20081218-160000",
"pagecounts-20081218-170000",
"pagecounts-20081218-180000",
"pagecounts-20081218-190001",
"pagecounts-20081218-200000",
"pagecounts-20081218-210000",
"pagecounts-20081218-220000",
"pagecounts-20081218-230000",
"pagecounts-20081219-000000",
"pagecounts-20081219-010001",
"pagecounts-20081219-020000",
"pagecounts-20081219-030000",
"pagecounts-20081219-040000",
"pagecounts-20081219-050000",
"pagecounts-20081219-060000",
"pagecounts-20081219-070001",
"pagecounts-20081219-080000",
"pagecounts-20081219-090000",
"pagecounts-20081219-100000",
"pagecounts-20081219-110000",
"pagecounts-20081219-120000",
"pagecounts-20081219-130001",
"pagecounts-20081219-140000",
"pagecounts-20081219-150000",
"pagecounts-20081219-160000",
"pagecounts-20081219-170000",
"pagecounts-20081219-180000",
"pagecounts-20081219-190001",
"pagecounts-20081219-200000",
"pagecounts-20081219-210000",
"pagecounts-20081219-220000",
"pagecounts-20081219-230000",
"pagecounts-20081220-000000",
"pagecounts-20081220-010001",
"pagecounts-20081220-020000",
"pagecounts-20081220-030000",
"pagecounts-20081220-040000",
"pagecounts-20081220-050000",
"pagecounts-20081220-060000",
"pagecounts-20081220-070001",
"pagecounts-20081220-080000",
"pagecounts-20081220-090000",
"pagecounts-20081220-100000",
"pagecounts-20081220-110000",
"pagecounts-20081220-120000",
"pagecounts-20081220-130001",
"pagecounts-20081220-140000",
"pagecounts-20081220-150000",
"pagecounts-20081220-160000",
"pagecounts-20081220-170000",
"pagecounts-20081220-180000",
"pagecounts-20081220-190001",
"pagecounts-20081220-200000",
"pagecounts-20081220-210000",
"pagecounts-20081220-220000",
"pagecounts-20081220-230000",
"pagecounts-20081221-000000",
"pagecounts-20081221-010001",
"pagecounts-20081221-020000",
"pagecounts-20081221-030000",
"pagecounts-20081221-040000",
"pagecounts-20081221-050000",
"pagecounts-20081221-060000",
"pagecounts-20081221-070001",
"pagecounts-20081221-080000",
"pagecounts-20081221-090000",
"pagecounts-20081221-100000",
"pagecounts-20081221-110000",
"pagecounts-20081221-120000",
"pagecounts-20081221-130001",
"pagecounts-20081221-140000",
"pagecounts-20081221-150000",
"pagecounts-20081221-160000",
"pagecounts-20081221-170000",
"pagecounts-20081221-180000",
"pagecounts-20081221-190001",
"pagecounts-20081221-200000",
"pagecounts-20081221-210000",
"pagecounts-20081221-220000",
"pagecounts-20081221-230000",
"pagecounts-20081222-000000",
"pagecounts-20081222-010001",
"pagecounts-20081222-020000",
"pagecounts-20081222-030000",
"pagecounts-20081222-040000",
"pagecounts-20081222-050000",
"pagecounts-20081222-060000",
"pagecounts-20081222-070001",
"pagecounts-20081222-080000",
"pagecounts-20081222-090000",
"pagecounts-20081222-100000",
"pagecounts-20081222-110000",
"pagecounts-20081222-120000",
"pagecounts-20081222-130001",
"pagecounts-20081222-140000",
"pagecounts-20081222-150000",
"pagecounts-20081222-160000",
"pagecounts-20081222-170000",
"pagecounts-20081222-180000",
"pagecounts-20081222-190001",
"pagecounts-20081222-200000",
"pagecounts-20081222-210000",
"pagecounts-20081222-220000",
"pagecounts-20081222-230000",
"pagecounts-20081223-000000",
"pagecounts-20081223-010001",
"pagecounts-20081223-020000",
"pagecounts-20081223-030000",
"pagecounts-20081223-040000",
"pagecounts-20081223-050000",
"pagecounts-20081223-060000",
"pagecounts-20081223-070001",
"pagecounts-20081223-080000",
"pagecounts-20081223-090000",
"pagecounts-20081223-100000",
"pagecounts-20081223-110000",
"pagecounts-20081223-120000",
"pagecounts-20081223-130001",
"pagecounts-20081223-140000",
"pagecounts-20081223-150000",
"pagecounts-20081223-160000",
"pagecounts-20081223-170000",
"pagecounts-20081223-180000",
"pagecounts-20081223-190001",
"pagecounts-20081223-200000",
"pagecounts-20081223-210000",
"pagecounts-20081223-220000",
"pagecounts-20081223-230000",
"pagecounts-20081224-000000",
"pagecounts-20081224-010001",
"pagecounts-20081224-020000",
"pagecounts-20081224-030000",
"pagecounts-20081224-040000",
"pagecounts-20081224-050000",
"pagecounts-20081224-060000",
"pagecounts-20081224-070001",
"pagecounts-20081224-080000",
"pagecounts-20081224-090000",
"pagecounts-20081224-100000",
"pagecounts-20081224-110000",
"pagecounts-20081224-120000",
"pagecounts-20081224-130001",
"pagecounts-20081224-140000",
"pagecounts-20081224-150000",
"pagecounts-20081224-160000",
"pagecounts-20081224-170000",
"pagecounts-20081224-180000",
"pagecounts-20081224-190001",
"pagecounts-20081224-200000",
"pagecounts-20081224-210000",
"pagecounts-20081224-220000",
"pagecounts-20081224-230000",
"pagecounts-20081225-000000",
"pagecounts-20081225-010001",
"pagecounts-20081225-020000",
"pagecounts-20081225-030000",
"pagecounts-20081225-040000",
"pagecounts-20081225-050000",
"pagecounts-20081225-060000",
"pagecounts-20081225-070001",
"pagecounts-20081225-080000",
"pagecounts-20081225-090000",
"pagecounts-20081225-100000",
"pagecounts-20081225-110000",
"pagecounts-20081225-120000",
"pagecounts-20081225-130001",
"pagecounts-20081225-140000",
"pagecounts-20081225-150000",
"pagecounts-20081225-160000",
"pagecounts-20081225-170000",
"pagecounts-20081225-180000",
"pagecounts-20081225-190001",
"pagecounts-20081225-200000",
"pagecounts-20081225-210000",
"pagecounts-20081225-220000",
"pagecounts-20081225-230000",
"pagecounts-20081226-000000",
"pagecounts-20081226-010001",
"pagecounts-20081226-020000",
"pagecounts-20081226-030000",
"pagecounts-20081226-040000",
"pagecounts-20081226-050000",
"pagecounts-20081226-060000",
"pagecounts-20081226-070001",
"pagecounts-20081226-080000",
"pagecounts-20081226-090000",
"pagecounts-20081226-100000",
"pagecounts-20081226-110000",
"pagecounts-20081226-120000",
"pagecounts-20081226-130000",
"pagecounts-20081226-140001",
"pagecounts-20081226-150000",
"pagecounts-20081226-160000",
"pagecounts-20081226-170000",
"pagecounts-20081226-180000",
"pagecounts-20081226-190000",
"pagecounts-20081226-200001",
"pagecounts-20081226-210000",
"pagecounts-20081226-220000",
"pagecounts-20081226-230000",
"pagecounts-20081227-000000",
"pagecounts-20081227-010000",
"pagecounts-20081227-020001",
"pagecounts-20081227-030000",
"pagecounts-20081227-040000",
"pagecounts-20081227-050000",
"pagecounts-20081227-060000",
"pagecounts-20081227-070000",
"pagecounts-20081227-080001",
"pagecounts-20081227-090000",
"pagecounts-20081227-100000",
"pagecounts-20081227-110000",
"pagecounts-20081227-120000",
"pagecounts-20081227-130000",
"pagecounts-20081227-140001",
"pagecounts-20081227-150000",
"pagecounts-20081227-160000",
"pagecounts-20081227-170000",
"pagecounts-20081227-180000",
"pagecounts-20081227-190000",
"pagecounts-20081227-200001",
"pagecounts-20081227-210000",
"pagecounts-20081227-220000",
"pagecounts-20081227-230000",
"pagecounts-20081228-000000",
"pagecounts-20081228-010000",
"pagecounts-20081228-020001",
"pagecounts-20081228-030000",
"pagecounts-20081228-040000",
"pagecounts-20081228-050000",
"pagecounts-20081228-060000",
"pagecounts-20081228-070000",
"pagecounts-20081228-080001",
"pagecounts-20081228-090000",
"pagecounts-20081228-100000",
"pagecounts-20081228-110000",
"pagecounts-20081228-120000",
"pagecounts-20081228-130000",
"pagecounts-20081228-140001",
"pagecounts-20081228-150000",
"pagecounts-20081228-160000",
"pagecounts-20081228-170000",
"pagecounts-20081228-180000",
"pagecounts-20081228-190000",
"pagecounts-20081228-200001",
"pagecounts-20081228-210000",
"pagecounts-20081228-220000",
"pagecounts-20081228-230000",
"pagecounts-20081229-000000",
"pagecounts-20081229-010000",
"pagecounts-20081229-020001",
"pagecounts-20081229-030000",
"pagecounts-20081229-040000",
"pagecounts-20081229-050000",
"pagecounts-20081229-060000",
"pagecounts-20081229-070000",
"pagecounts-20081229-080001",
"pagecounts-20081229-090000",
"pagecounts-20081229-100000",
"pagecounts-20081229-110000",
"pagecounts-20081229-120000",
"pagecounts-20081229-130000",
"pagecounts-20081229-140001",
"pagecounts-20081229-150000",
"pagecounts-20081229-160000",
"pagecounts-20081229-170000",
"pagecounts-20081229-180000",
"pagecounts-20081229-190000",
"pagecounts-20081229-200001",
"pagecounts-20081229-210000",
"pagecounts-20081229-220000",
"pagecounts-20081229-230000",
"pagecounts-20081230-000000",
"pagecounts-20081230-010000",
"pagecounts-20081230-020001",
"pagecounts-20081230-030000",
"pagecounts-20081230-040000",
"pagecounts-20081230-050000",
"pagecounts-20081230-060000",
"pagecounts-20081230-070000",
"pagecounts-20081230-080001",
"pagecounts-20081230-090000",
"pagecounts-20081230-100000",
"pagecounts-20081230-110000",
"pagecounts-20081230-120000",
"pagecounts-20081230-130000",
"pagecounts-20081230-140001",
"pagecounts-20081230-150000",
"pagecounts-20081230-160000",
"pagecounts-20081230-170000",
"pagecounts-20081230-180000",
"pagecounts-20081230-190000",
"pagecounts-20081230-200001",
"pagecounts-20081230-210000",
"pagecounts-20081230-220000",
"pagecounts-20081230-230000",
"pagecounts-20081231-000000",
"pagecounts-20081231-010000",
"pagecounts-20081231-020000",
"pagecounts-20081231-030001",
"pagecounts-20081231-040000",
"pagecounts-20081231-050000",
"pagecounts-20081231-060000",
"pagecounts-20081231-070000",
"pagecounts-20081231-080000",
"pagecounts-20081231-090001",
"pagecounts-20081231-100000",
"pagecounts-20081231-110000",
"pagecounts-20081231-120000",
"pagecounts-20081231-130000",
"pagecounts-20081231-140000",
"pagecounts-20081231-150001",
"pagecounts-20081231-160000",
"pagecounts-20081231-170000",
"pagecounts-20081231-180000",
"pagecounts-20081231-190000",
"pagecounts-20081231-200000",
"pagecounts-20081231-210001",
"pagecounts-20081231-220000",
"pagecounts-20081231-230000",
"pagecounts-20081231-235959",
]

base = "http://dumps.wikimedia.org/other/pagecounts-raw/"
tail = "2008/2008-12/"

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
