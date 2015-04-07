from __future__ import with_statement
import os

urls = [
"pagecounts-20081001-000000",
"pagecounts-20081001-010000",
"pagecounts-20081001-020000",
"pagecounts-20081001-030000",
"pagecounts-20081001-040000",
"pagecounts-20081001-050001",
"pagecounts-20081001-060000",
"pagecounts-20081001-070000",
"pagecounts-20081001-080000",
"pagecounts-20081001-090000",
"pagecounts-20081001-100000",
"pagecounts-20081001-110001",
"pagecounts-20081001-120000",
"pagecounts-20081001-130000",
"pagecounts-20081001-140000",
"pagecounts-20081001-150000",
"pagecounts-20081001-160000",
"pagecounts-20081001-170001",
"pagecounts-20081001-180000",
"pagecounts-20081001-190000",
"pagecounts-20081001-200000",
"pagecounts-20081001-210000",
"pagecounts-20081001-220000",
"pagecounts-20081001-230001",
"pagecounts-20081002-000000",
"pagecounts-20081002-010000",
"pagecounts-20081002-020000",
"pagecounts-20081002-030000",
"pagecounts-20081002-040000",
"pagecounts-20081002-050001",
"pagecounts-20081002-060000",
"pagecounts-20081002-070000",
"pagecounts-20081002-080000",
"pagecounts-20081002-090000",
"pagecounts-20081002-100000",
"pagecounts-20081002-110001",
"pagecounts-20081002-120000",
"pagecounts-20081002-130000",
"pagecounts-20081002-140000",
"pagecounts-20081002-150000",
"pagecounts-20081002-160000",
"pagecounts-20081002-170001",
"pagecounts-20081002-180000",
"pagecounts-20081002-190000",
"pagecounts-20081002-200000",
"pagecounts-20081002-210000",
"pagecounts-20081002-220000",
"pagecounts-20081002-230001",
"pagecounts-20081003-000000",
"pagecounts-20081003-010000",
"pagecounts-20081003-020000",
"pagecounts-20081003-030000",
"pagecounts-20081003-040000",
"pagecounts-20081003-050001",
"pagecounts-20081003-060000",
"pagecounts-20081003-070000",
"pagecounts-20081003-080000",
"pagecounts-20081003-090000",
"pagecounts-20081003-100000",
"pagecounts-20081003-110001",
"pagecounts-20081003-120000",
"pagecounts-20081003-130000",
"pagecounts-20081003-140000",
"pagecounts-20081003-150000",
"pagecounts-20081003-160001",
"pagecounts-20081003-170000",
"pagecounts-20081003-180000",
"pagecounts-20081003-190000",
"pagecounts-20081003-200000",
"pagecounts-20081003-210000",
"pagecounts-20081003-220001",
"pagecounts-20081003-230000",
"pagecounts-20081004-000000",
"pagecounts-20081004-010000",
"pagecounts-20081004-020000",
"pagecounts-20081004-030000",
"pagecounts-20081004-040001",
"pagecounts-20081004-050000",
"pagecounts-20081004-060000",
"pagecounts-20081004-070000",
"pagecounts-20081004-080000",
"pagecounts-20081004-090000",
"pagecounts-20081004-100001",
"pagecounts-20081004-110000",
"pagecounts-20081004-120000",
"pagecounts-20081004-130000",
"pagecounts-20081004-140000",
"pagecounts-20081004-150000",
"pagecounts-20081004-160001",
"pagecounts-20081004-170000",
"pagecounts-20081004-180000",
"pagecounts-20081004-190000",
"pagecounts-20081004-200000",
"pagecounts-20081004-210000",
"pagecounts-20081004-220001",
"pagecounts-20081004-230000",
"pagecounts-20081005-000000",
"pagecounts-20081005-010000",
"pagecounts-20081005-020000",
"pagecounts-20081005-030000",
"pagecounts-20081005-040001",
"pagecounts-20081005-050000",
"pagecounts-20081005-060000",
"pagecounts-20081005-070000",
"pagecounts-20081005-080000",
"pagecounts-20081005-090000",
"pagecounts-20081005-100001",
"pagecounts-20081005-110000",
"pagecounts-20081005-120000",
"pagecounts-20081005-130000",
"pagecounts-20081005-140000",
"pagecounts-20081005-150000",
"pagecounts-20081005-160001",
"pagecounts-20081005-170000",
"pagecounts-20081005-180000",
"pagecounts-20081005-190000",
"pagecounts-20081005-200000",
"pagecounts-20081005-210000",
"pagecounts-20081005-220001",
"pagecounts-20081005-230000",
"pagecounts-20081006-000000",
"pagecounts-20081006-010000",
"pagecounts-20081006-020000",
"pagecounts-20081006-030000",
"pagecounts-20081006-040001",
"pagecounts-20081006-050000",
"pagecounts-20081006-060000",
"pagecounts-20081006-070000",
"pagecounts-20081006-080000",
"pagecounts-20081006-090000",
"pagecounts-20081006-100001",
"pagecounts-20081006-110000",
"pagecounts-20081006-120000",
"pagecounts-20081006-130000",
"pagecounts-20081006-140000",
"pagecounts-20081006-150000",
"pagecounts-20081006-160001",
"pagecounts-20081006-170000",
"pagecounts-20081006-180000",
"pagecounts-20081006-190000",
"pagecounts-20081006-200000",
"pagecounts-20081006-210000",
"pagecounts-20081006-220001",
"pagecounts-20081006-230000",
"pagecounts-20081007-000000",
"pagecounts-20081007-010000",
"pagecounts-20081007-020000",
"pagecounts-20081007-030000",
"pagecounts-20081007-040001",
"pagecounts-20081007-050000",
"pagecounts-20081007-060000",
"pagecounts-20081007-070000",
"pagecounts-20081007-080000",
"pagecounts-20081007-090000",
"pagecounts-20081007-100001",
"pagecounts-20081007-110000",
"pagecounts-20081007-120000",
"pagecounts-20081007-130000",
"pagecounts-20081007-140000",
"pagecounts-20081007-150001",
"pagecounts-20081007-160000",
"pagecounts-20081007-170000",
"pagecounts-20081007-180000",
"pagecounts-20081007-190000",
"pagecounts-20081007-200000",
"pagecounts-20081007-210001",
"pagecounts-20081007-220000",
"pagecounts-20081007-230000",
"pagecounts-20081008-000000",
"pagecounts-20081008-010000",
"pagecounts-20081008-020000",
"pagecounts-20081008-030001",
"pagecounts-20081008-040000",
"pagecounts-20081008-050000",
"pagecounts-20081008-060000",
"pagecounts-20081008-070000",
"pagecounts-20081008-080000",
"pagecounts-20081008-090001",
"pagecounts-20081008-100000",
"pagecounts-20081008-110000",
"pagecounts-20081008-120000",
"pagecounts-20081008-130000",
"pagecounts-20081008-140000",
"pagecounts-20081008-150001",
"pagecounts-20081008-160000",
"pagecounts-20081008-170000",
"pagecounts-20081008-180000",
"pagecounts-20081008-190000",
"pagecounts-20081008-200000",
"pagecounts-20081008-210001",
"pagecounts-20081008-220000",
"pagecounts-20081008-230000",
"pagecounts-20081009-000000",
"pagecounts-20081009-010000",
"pagecounts-20081009-020001",
"pagecounts-20081009-030000",
"pagecounts-20081009-040000",
"pagecounts-20081009-050000",
"pagecounts-20081009-060000",
"pagecounts-20081009-070000",
"pagecounts-20081009-080001",
"pagecounts-20081009-090000",
"pagecounts-20081009-100000",
"pagecounts-20081009-110000",
"pagecounts-20081009-120000",
"pagecounts-20081009-130000",
"pagecounts-20081009-140001",
"pagecounts-20081009-150000",
"pagecounts-20081009-160000",
"pagecounts-20081009-170000",
"pagecounts-20081009-180000",
"pagecounts-20081009-190000",
"pagecounts-20081009-200001",
"pagecounts-20081009-210000",
"pagecounts-20081009-220000",
"pagecounts-20081009-230000",
"pagecounts-20081010-000000",
"pagecounts-20081010-010000",
"pagecounts-20081010-020001",
"pagecounts-20081010-030000",
"pagecounts-20081010-040000",
"pagecounts-20081010-050000",
"pagecounts-20081010-060000",
"pagecounts-20081010-070001",
"pagecounts-20081010-080000",
"pagecounts-20081010-090000",
"pagecounts-20081010-100000",
"pagecounts-20081010-110000",
"pagecounts-20081010-120000",
"pagecounts-20081010-130001",
"pagecounts-20081010-140000",
"pagecounts-20081010-150000",
"pagecounts-20081010-160000",
"pagecounts-20081010-170000",
"pagecounts-20081010-180000",
"pagecounts-20081010-190001",
"pagecounts-20081010-200000",
"pagecounts-20081010-210000",
"pagecounts-20081010-220000",
"pagecounts-20081010-230000",
"pagecounts-20081011-000000",
"pagecounts-20081011-010001",
"pagecounts-20081011-020000",
"pagecounts-20081011-030000",
"pagecounts-20081011-040000",
"pagecounts-20081011-050000",
"pagecounts-20081011-060000",
"pagecounts-20081011-070001",
"pagecounts-20081011-080000",
"pagecounts-20081011-090000",
"pagecounts-20081011-100000",
"pagecounts-20081011-110000",
"pagecounts-20081011-120000",
"pagecounts-20081011-130001",
"pagecounts-20081011-140000",
"pagecounts-20081011-150000",
"pagecounts-20081011-160000",
"pagecounts-20081011-170000",
"pagecounts-20081011-180000",
"pagecounts-20081011-190001",
"pagecounts-20081011-200000",
"pagecounts-20081011-210000",
"pagecounts-20081011-220000",
"pagecounts-20081011-230000",
"pagecounts-20081012-000000",
"pagecounts-20081012-010001",
"pagecounts-20081012-020000",
"pagecounts-20081012-030000",
"pagecounts-20081012-040000",
"pagecounts-20081012-050000",
"pagecounts-20081012-060000",
"pagecounts-20081012-070001",
"pagecounts-20081012-080000",
"pagecounts-20081012-090000",
"pagecounts-20081012-100000",
"pagecounts-20081012-110000",
"pagecounts-20081012-120000",
"pagecounts-20081012-130001",
"pagecounts-20081012-140000",
"pagecounts-20081012-150000",
"pagecounts-20081012-160000",
"pagecounts-20081012-170000",
"pagecounts-20081012-180000",
"pagecounts-20081012-190001",
"pagecounts-20081012-200000",
"pagecounts-20081012-210000",
"pagecounts-20081012-220000",
"pagecounts-20081012-230000",
"pagecounts-20081013-000000",
"pagecounts-20081013-010001",
"pagecounts-20081013-020000",
"pagecounts-20081013-030000",
"pagecounts-20081013-040000",
"pagecounts-20081013-050000",
"pagecounts-20081013-060000",
"pagecounts-20081013-070001",
"pagecounts-20081013-080000",
"pagecounts-20081013-090000",
"pagecounts-20081013-100000",
"pagecounts-20081013-110000",
"pagecounts-20081013-120000",
"pagecounts-20081013-130001",
"pagecounts-20081013-140000",
"pagecounts-20081013-150000",
"pagecounts-20081013-160000",
"pagecounts-20081013-170000",
"pagecounts-20081013-180000",
"pagecounts-20081013-190001",
"pagecounts-20081013-200000",
"pagecounts-20081013-210000",
"pagecounts-20081013-220000",
"pagecounts-20081013-230000",
"pagecounts-20081014-000001",
"pagecounts-20081014-010000",
"pagecounts-20081014-020000",
"pagecounts-20081014-030000",
"pagecounts-20081014-040000",
"pagecounts-20081014-050000",
"pagecounts-20081014-060001",
"pagecounts-20081014-070000",
"pagecounts-20081014-080000",
"pagecounts-20081014-090000",
"pagecounts-20081014-100000",
"pagecounts-20081014-110000",
"pagecounts-20081014-120001",
"pagecounts-20081014-130000",
"pagecounts-20081014-140000",
"pagecounts-20081014-150000",
"pagecounts-20081014-160000",
"pagecounts-20081014-170000",
"pagecounts-20081014-180001",
"pagecounts-20081014-190000",
"pagecounts-20081014-200000",
"pagecounts-20081014-210000",
"pagecounts-20081014-220000",
"pagecounts-20081014-230000",
"pagecounts-20081015-000001",
"pagecounts-20081015-010000",
"pagecounts-20081015-020000",
"pagecounts-20081015-030000",
"pagecounts-20081015-040000",
"pagecounts-20081015-050001",
"pagecounts-20081015-060000",
"pagecounts-20081015-070000",
"pagecounts-20081015-080000",
"pagecounts-20081015-090000",
"pagecounts-20081015-100000",
"pagecounts-20081015-110001",
"pagecounts-20081015-120000",
"pagecounts-20081015-130000",
"pagecounts-20081015-140000",
"pagecounts-20081015-150000",
"pagecounts-20081015-160000",
"pagecounts-20081015-170001",
"pagecounts-20081015-180000",
"pagecounts-20081015-190000",
"pagecounts-20081015-200000",
"pagecounts-20081015-210000",
"pagecounts-20081015-220000",
"pagecounts-20081015-230001",
"pagecounts-20081016-000000",
"pagecounts-20081016-010000",
"pagecounts-20081016-020000",
"pagecounts-20081016-030000",
"pagecounts-20081016-040000",
"pagecounts-20081016-050001",
"pagecounts-20081016-060000",
"pagecounts-20081016-070000",
"pagecounts-20081016-080000",
"pagecounts-20081016-090000",
"pagecounts-20081016-100001",
"pagecounts-20081016-110000",
"pagecounts-20081016-120000",
"pagecounts-20081016-130000",
"pagecounts-20081016-140000",
"pagecounts-20081016-150000",
"pagecounts-20081016-160001",
"pagecounts-20081016-170000",
"pagecounts-20081016-180000",
"pagecounts-20081016-190000",
"pagecounts-20081016-200000",
"pagecounts-20081016-210000",
"pagecounts-20081016-220001",
"pagecounts-20081016-230000",
"pagecounts-20081017-000000",
"pagecounts-20081017-010000",
"pagecounts-20081017-020000",
"pagecounts-20081017-030000",
"pagecounts-20081017-040001",
"pagecounts-20081017-050000",
"pagecounts-20081017-060000",
"pagecounts-20081017-070000",
"pagecounts-20081017-080000",
"pagecounts-20081017-090000",
"pagecounts-20081017-100001",
"pagecounts-20081017-110000",
"pagecounts-20081017-120000",
"pagecounts-20081017-130000",
"pagecounts-20081017-140000",
"pagecounts-20081017-150000",
"pagecounts-20081017-160001",
"pagecounts-20081017-170000",
"pagecounts-20081017-180000",
"pagecounts-20081017-190000",
"pagecounts-20081017-200000",
"pagecounts-20081017-210001",
"pagecounts-20081017-220000",
"pagecounts-20081017-230000",
"pagecounts-20081018-000000",
"pagecounts-20081018-010000",
"pagecounts-20081018-020000",
"pagecounts-20081018-030001",
"pagecounts-20081018-040000",
"pagecounts-20081018-050000",
"pagecounts-20081018-060000",
"pagecounts-20081018-070000",
"pagecounts-20081018-080000",
"pagecounts-20081018-090001",
"pagecounts-20081018-100000",
"pagecounts-20081018-110000",
"pagecounts-20081018-120000",
"pagecounts-20081018-130000",
"pagecounts-20081018-140000",
"pagecounts-20081018-150001",
"pagecounts-20081018-160000",
"pagecounts-20081018-170000",
"pagecounts-20081018-180000",
"pagecounts-20081018-190000",
"pagecounts-20081018-200001",
"pagecounts-20081018-210000",
"pagecounts-20081018-220000",
"pagecounts-20081018-230000",
"pagecounts-20081019-000000",
"pagecounts-20081019-010000",
"pagecounts-20081019-020001",
"pagecounts-20081019-030000",
"pagecounts-20081019-040000",
"pagecounts-20081019-050000",
"pagecounts-20081019-060000",
"pagecounts-20081019-070000",
"pagecounts-20081019-080001",
"pagecounts-20081019-090000",
"pagecounts-20081019-100000",
"pagecounts-20081019-110000",
"pagecounts-20081019-120000",
"pagecounts-20081019-130000",
"pagecounts-20081019-140001",
"pagecounts-20081019-150000",
"pagecounts-20081019-160000",
"pagecounts-20081019-170000",
"pagecounts-20081019-180000",
"pagecounts-20081019-190000",
"pagecounts-20081019-200001",
"pagecounts-20081019-210000",
"pagecounts-20081019-220000",
"pagecounts-20081019-230000",
"pagecounts-20081020-000000",
"pagecounts-20081020-010001",
"pagecounts-20081020-020000",
"pagecounts-20081020-030000",
"pagecounts-20081020-040000",
"pagecounts-20081020-050000",
"pagecounts-20081020-060000",
"pagecounts-20081020-070001",
"pagecounts-20081020-080000",
"pagecounts-20081020-090000",
"pagecounts-20081020-100000",
"pagecounts-20081020-110000",
"pagecounts-20081020-120000",
"pagecounts-20081020-130001",
"pagecounts-20081020-140000",
"pagecounts-20081020-150000",
"pagecounts-20081020-160000",
"pagecounts-20081020-170000",
"pagecounts-20081020-180000",
"pagecounts-20081020-190001",
"pagecounts-20081020-200000",
"pagecounts-20081020-210000",
"pagecounts-20081020-220000",
"pagecounts-20081020-230000",
"pagecounts-20081021-000001",
"pagecounts-20081021-010000",
"pagecounts-20081021-020000",
"pagecounts-20081021-030000",
"pagecounts-20081021-040000",
"pagecounts-20081021-050000",
"pagecounts-20081021-060001",
"pagecounts-20081021-070000",
"pagecounts-20081021-080000",
"pagecounts-20081021-090000",
"pagecounts-20081021-100000",
"pagecounts-20081021-110000",
"pagecounts-20081021-120001",
"pagecounts-20081021-130000",
"pagecounts-20081021-140001",
"pagecounts-20081022-120000",
"pagecounts-20081022-130000",
"pagecounts-20081022-140000",
"pagecounts-20081022-150000",
"pagecounts-20081022-160000",
"pagecounts-20081022-170001",
"pagecounts-20081022-180000",
"pagecounts-20081022-190000",
"pagecounts-20081022-200000",
"pagecounts-20081022-210000",
"pagecounts-20081022-220000",
"pagecounts-20081022-230000",
"pagecounts-20081023-000001",
"pagecounts-20081023-010000",
"pagecounts-20081023-020000",
"pagecounts-20081023-030000",
"pagecounts-20081023-040000",
"pagecounts-20081023-050000",
"pagecounts-20081023-060001",
"pagecounts-20081023-070000",
"pagecounts-20081023-080000",
"pagecounts-20081023-090000",
"pagecounts-20081023-100000",
"pagecounts-20081023-110000",
"pagecounts-20081023-120001",
"pagecounts-20081023-130000",
"pagecounts-20081023-140000",
"pagecounts-20081023-150000",
"pagecounts-20081023-160000",
"pagecounts-20081023-170000",
"pagecounts-20081023-180001",
"pagecounts-20081023-190000",
"pagecounts-20081023-200000",
"pagecounts-20081023-210000",
"pagecounts-20081023-220000",
"pagecounts-20081023-230000",
"pagecounts-20081024-000001",
"pagecounts-20081024-010000",
"pagecounts-20081024-020000",
"pagecounts-20081024-030000",
"pagecounts-20081024-040000",
"pagecounts-20081024-050000",
"pagecounts-20081024-060001",
"pagecounts-20081024-070000",
"pagecounts-20081024-080000",
"pagecounts-20081024-090000",
"pagecounts-20081024-100000",
"pagecounts-20081024-110000",
"pagecounts-20081024-120001",
"pagecounts-20081024-130000",
"pagecounts-20081024-140000",
"pagecounts-20081024-150000",
"pagecounts-20081024-160000",
"pagecounts-20081024-170000",
"pagecounts-20081024-180001",
"pagecounts-20081024-190000",
"pagecounts-20081024-200000",
"pagecounts-20081024-210000",
"pagecounts-20081024-220000",
"pagecounts-20081024-230000",
"pagecounts-20081025-000001",
"pagecounts-20081025-010000",
"pagecounts-20081025-020000",
"pagecounts-20081025-030000",
"pagecounts-20081025-040000",
"pagecounts-20081025-050000",
"pagecounts-20081025-060001",
"pagecounts-20081025-070000",
"pagecounts-20081025-080000",
"pagecounts-20081025-090000",
"pagecounts-20081025-100000",
"pagecounts-20081025-110000",
"pagecounts-20081025-120001",
"pagecounts-20081025-130000",
"pagecounts-20081025-140000",
"pagecounts-20081025-150000",
"pagecounts-20081025-160000",
"pagecounts-20081025-170000",
"pagecounts-20081025-180001",
"pagecounts-20081025-190000",
"pagecounts-20081025-200000",
"pagecounts-20081025-210000",
"pagecounts-20081025-220000",
"pagecounts-20081025-230000",
"pagecounts-20081026-000001",
"pagecounts-20081026-010000",
"pagecounts-20081026-020000",
"pagecounts-20081026-030000",
"pagecounts-20081026-040000",
"pagecounts-20081026-050000",
"pagecounts-20081026-060001",
"pagecounts-20081026-070000",
"pagecounts-20081026-080000",
"pagecounts-20081026-090000",
"pagecounts-20081026-100000",
"pagecounts-20081026-110000",
"pagecounts-20081026-120001",
"pagecounts-20081026-130000",
"pagecounts-20081026-140000",
"pagecounts-20081026-150000",
"pagecounts-20081026-160000",
"pagecounts-20081026-170000",
"pagecounts-20081026-180001",
"pagecounts-20081026-190000",
"pagecounts-20081026-200000",
"pagecounts-20081026-210000",
"pagecounts-20081026-220000",
"pagecounts-20081026-230000",
"pagecounts-20081027-000001",
"pagecounts-20081027-010000",
"pagecounts-20081027-020000",
"pagecounts-20081027-030000",
"pagecounts-20081027-040000",
"pagecounts-20081027-050000",
"pagecounts-20081027-060001",
"pagecounts-20081027-070000",
"pagecounts-20081027-080000",
"pagecounts-20081027-090000",
"pagecounts-20081027-100000",
"pagecounts-20081027-110000",
"pagecounts-20081027-120001",
"pagecounts-20081027-130000",
"pagecounts-20081027-140000",
"pagecounts-20081027-150000",
"pagecounts-20081027-160000",
"pagecounts-20081027-170000",
"pagecounts-20081027-180001",
"pagecounts-20081027-190000",
"pagecounts-20081027-200000",
"pagecounts-20081027-210000",
"pagecounts-20081027-220000",
"pagecounts-20081027-230000",
"pagecounts-20081028-000001",
"pagecounts-20081028-010000",
"pagecounts-20081028-020000",
"pagecounts-20081028-030000",
"pagecounts-20081028-040000",
"pagecounts-20081028-050000",
"pagecounts-20081028-060001",
"pagecounts-20081028-070000",
"pagecounts-20081028-080000",
"pagecounts-20081028-090000",
"pagecounts-20081028-100000",
"pagecounts-20081028-110000",
"pagecounts-20081028-120001",
"pagecounts-20081028-130000",
"pagecounts-20081028-140000",
"pagecounts-20081028-150000",
"pagecounts-20081028-160000",
"pagecounts-20081028-170000",
"pagecounts-20081028-180001",
"pagecounts-20081028-190000",
"pagecounts-20081028-200000",
"pagecounts-20081028-210000",
"pagecounts-20081028-220000",
"pagecounts-20081028-230000",
"pagecounts-20081029-000001",
"pagecounts-20081029-010000",
"pagecounts-20081029-020000",
"pagecounts-20081029-030000",
"pagecounts-20081029-040000",
"pagecounts-20081029-050000",
"pagecounts-20081029-060001",
"pagecounts-20081029-070000",
"pagecounts-20081029-080000",
"pagecounts-20081029-090000",
"pagecounts-20081029-100000",
"pagecounts-20081029-110000",
"pagecounts-20081029-120001",
"pagecounts-20081029-130000",
"pagecounts-20081029-140000",
"pagecounts-20081029-150000",
"pagecounts-20081029-160000",
"pagecounts-20081029-170000",
"pagecounts-20081029-180001",
"pagecounts-20081029-190000",
"pagecounts-20081029-200000",
"pagecounts-20081029-210000",
"pagecounts-20081029-220000",
"pagecounts-20081029-230000",
"pagecounts-20081030-000001",
"pagecounts-20081030-010000",
"pagecounts-20081030-020000",
"pagecounts-20081030-030000",
"pagecounts-20081030-040000",
"pagecounts-20081030-050000",
"pagecounts-20081030-060001",
"pagecounts-20081030-070000",
"pagecounts-20081030-080000",
"pagecounts-20081030-090000",
"pagecounts-20081030-100000",
"pagecounts-20081030-110000",
"pagecounts-20081030-120001",
"pagecounts-20081030-130000",
"pagecounts-20081030-140000",
"pagecounts-20081030-150000",
"pagecounts-20081030-160000",
"pagecounts-20081030-170000",
"pagecounts-20081030-180001",
"pagecounts-20081030-190000",
"pagecounts-20081030-200000",
"pagecounts-20081030-210000",
"pagecounts-20081030-220000",
"pagecounts-20081030-230000",
"pagecounts-20081031-000001",
"pagecounts-20081031-010000",
"pagecounts-20081031-020000",
"pagecounts-20081031-030000",
"pagecounts-20081031-040000",
"pagecounts-20081031-050000",
"pagecounts-20081031-060001",
"pagecounts-20081031-070000",
"pagecounts-20081031-080000",
"pagecounts-20081031-090000",
"pagecounts-20081031-100000",
"pagecounts-20081031-110000",
"pagecounts-20081031-120001",
"pagecounts-20081031-130000",
"pagecounts-20081031-140000",
"pagecounts-20081031-150000",
"pagecounts-20081031-160000",
"pagecounts-20081031-170000",
"pagecounts-20081031-180001",
"pagecounts-20081031-190000",
"pagecounts-20081031-200000",
"pagecounts-20081031-210000",
"pagecounts-20081031-220000",
"pagecounts-20081031-230000",
]

base = "http://dumps.wikimedia.org/other/pagecounts-raw/"
tail = "2008/2008-10/"

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
