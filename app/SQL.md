SELECT
    coverage_year,
    hios_issuer_id,
    MONTH(GAA_Load_Datetime) AS load_month,
    Insurance_Type,
    enrollment_status_description,
    enrollee_status_description,
    COUNT(*) AS row_count,
    COUNT(DISTINCT enrollment_id) AS enrollment_count,
    COUNT(DISTINCT enrollee_id) AS enrollee_count
FROM dbo.Enrollments_TEST
WHERE coverage_year = 2025
GROUP BY
    coverage_year,
    hios_issuer_id,
    MONTH(GAA_Load_Datetime),
    Insurance_Type,
    enrollment_status_description,
    enrollee_status_description
ORDER BY
    hios_issuer_id,
    load_month,
    enrollment_status_description,
    enrollee_status_description;


    2025	13535	6	Dental	Cancelled	Cancelled	935	702	908
2025	13535	6	Dental	Enrolled	Cancelled	2	2	2
2025	13535	6	Dental	Enrolled	Enrolled	1060	715	1060
2025	13535	6	Dental	Enrolled	Terminated	7	5	7
2025	13535	6	Dental	Pend canceled	Pend canceled	47	31	42
2025	13535	6	Dental	Pending	Pending	3	3	3
2025	13535	6	Dental	Terminated	Cancelled	5	5	5
2025	13535	6	Dental	Terminated	Terminated	592	405	586
2025	15105	6	Health	Aborted	Aborted	7	6	7
2025	15105	6	Health	Cancelled	Cancelled	20776	14659	18010
2025	15105	6	Health	Enrolled	Cancelled	77	59	73
2025	15105	6	Health	Enrolled	Enrolled	23063	17978	23063
2025	15105	6	Health	Enrolled	Terminated	133	110	131
2025	15105	6	Health	Pend	Pend	12	9	12
2025	15105	6	Health	Pend canceled	Enrolled	13	13	12
2025	15105	6	Health	Pend canceled	Pend canceled	557	412	487
2025	15105	6	Health	Terminated	Cancelled	86	64	85
2025	15105	6	Health	Terminated	Terminated	12097	9401	11387
2025	37001	6	Dental	Aborted	Aborted	2	2	2
2025	37001	6	Dental	Cancelled	Cancelled	5867	4345	5331
2025	37001	6	Dental	Cancelled	Pend canceled	2	1	2
2025	37001	6	Dental	Cancelled	Pending	3	3	3
2025	37001	6	Dental	Enrolled	Cancelled	7	7	7
2025	37001	6	Dental	Enrolled	Enrolled	3138	2307	3138
2025	37001	6	Dental	Enrolled	Terminated	24	23	24
2025	37001	6	Dental	Pend	Pend	1	1	1
2025	37001	6	Dental	Pend canceled	Pend canceled	124	98	110
2025	37001	6	Dental	Terminated	Cancelled	31	19	31
2025	37001	6	Dental	Terminated	Terminated	3197	2509	3156
2025	37301	6	Dental	Cancelled	Cancelled	4593	2930	4161
2025	37301	6	Dental	Cancelled	Pending	3	3	3
2025	37301	6	Dental	Enrolled	Cancelled	21	20	21
2025	37301	6	Dental	Enrolled	Enrolled	4260	2989	4260
2025	37301	6	Dental	Enrolled	Pending	1	1	1
2025	37301	6	Dental	Enrolled	Terminated	41	32	41
2025	37301	6	Dental	Pend	Pend	1	1	1
2025	37301	6	Dental	Pend canceled	Pend canceled	108	75	104
2025	37301	6	Dental	Terminated	Cancelled	28	18	28
2025	37301	6	Dental	Terminated	Pending	4	1	4
2025	37301	6	Dental	Terminated	Terminated	2673	1858	2646
2025	43802	6	Health	Aborted	Aborted	4	4	3
2025	43802	6	Dental	Aborted	Aborted	1	1	1
2025	43802	6	Health	Cancelled	Cancelled	3661	2354	3195
2025	43802	6	Dental	Cancelled	Cancelled	6171	4266	5942
2025	43802	6	Dental	Cancelled	Pend canceled	1	1	1
2025	43802	6	Dental	Cancelled	Pending	24	15	24
2025	43802	6	Health	Enrolled	Cancelled	15	13	15
2025	43802	6	Dental	Enrolled	Cancelled	36	24	36
2025	43802	6	Dental	Enrolled	Enrolled	8823	5868	8823
2025	43802	6	Health	Enrolled	Enrolled	5172	3874	5172
2025	43802	6	Health	Enrolled	Terminated	20	19	20
2025	43802	6	Dental	Enrolled	Terminated	84	69	84
2025	43802	6	Dental	Pend	Pend	3	3	3
2025	43802	6	Health	Pend	Pend	2	1	2
2025	43802	6	Health	Pend canceled	Pend canceled	358	268	306
2025	43802	6	Dental	Pend canceled	Pend canceled	559	322	521
2025	43802	6	Health	Pend canceled	Pending	3	1	3
2025	43802	6	Health	Pending	Pending	9	3	9
2025	43802	6	Dental	Pending	Pending	48	28	48
2025	43802	6	Health	Terminated	Cancelled	30	23	30
2025	43802	6	Dental	Terminated	Cancelled	46	33	45
2025	43802	6	Health	Terminated	Terminated	2886	2210	2763
2025	43802	6	Dental	Terminated	Terminated	5442	3465	5382
2025	45334	6	Health	Aborted	Aborted	61	53	57
2025	45334	6	Health	Cancelled	Cancelled	34958	28015	30212
2025	45334	6	Health	Enrolled	Aborted	1	1	1
2025	45334	6	Health	Enrolled	Cancelled	106	78	102
2025	45334	6	Health	Enrolled	Enrolled	63823	52905	63823
2025	45334	6	Health	Enrolled	Terminated	434	362	430
2025	45334	6	Health	Pend	Pend	71	55	69
2025	45334	6	Health	Pend canceled	Pend canceled	3483	2697	3059
2025	45334	6	Health	Pend canceled	Pending	8	5	8
2025	45334	6	Health	Pending	Pending	19	14	19
2025	45334	6	Health	Terminated	Cancelled	233	167	216
2025	45334	6	Health	Terminated	Terminated	58730	49122	54341
2025	49046	6	Health	Aborted	Aborted	18	13	18
2025	49046	6	Dental	Aborted	Aborted	3	2	3
2025	49046	6	Health	Cancelled	Aborted	1	1	1
2025	49046	6	Dental	Cancelled	Cancelled	23054	16038	21364
2025	49046	6	Health	Cancelled	Cancelled	39484	24975	33710
2025	49046	6	Dental	Cancelled	Pend canceled	1	1	1
2025	49046	6	Dental	Cancelled	Pending	30	20	30
2025	49046	6	Health	Enrolled	Aborted	2	2	2
2025	49046	6	Health	Enrolled	Cancelled	246	206	241
2025	49046	6	Dental	Enrolled	Cancelled	104	75	103
2025	49046	6	Dental	Enrolled	Enrolled	21258	14432	21256
2025	49046	6	Health	Enrolled	Enrolled	63296	44169	63296
2025	49046	6	Health	Enrolled	Terminated	546	464	543
2025	49046	6	Dental	Enrolled	Terminated	215	181	213
2025	49046	6	Health	Pend	Pend	26	19	26
2025	49046	6	Dental	Pend	Pend	14	9	14
2025	49046	6	Health	Pend canceled	Pend canceled	2069	1363	1850
2025	49046	6	Dental	Pend canceled	Pend canceled	1265	862	1169
2025	49046	6	Health	Pending	Pending	17	9	17
2025	49046	6	Dental	Pending	Pending	6	6	6
2025	49046	6	Health	Terminated	Aborted	4	2	4
2025	49046	6	Dental	Terminated	Cancelled	122	87	118
2025	49046	6	Health	Terminated	Cancelled	233	182	228
2025	49046	6	Dental	Terminated	Terminated	14916	10621	14753
2025	49046	6	Health	Terminated	Terminated	32745	24078	30526
2025	58081	6	Health	Aborted	Aborted	102	85	99
2025	58081	6	Health	Cancelled	Aborted	1	1	1
2025	58081	6	Health	Cancelled	Cancelled	210011	141401	174523
2025	58081	6	Health	Enrolled	Aborted	9	6	7
2025	58081	6	Health	Enrolled	Cancelled	970	748	941
2025	58081	6	Health	Enrolled	Enrolled	210311	150551	210311
2025	58081	6	Health	Enrolled	Terminated	2824	2181	2722
2025	58081	6	Health	Pend	Pend	43	32	43
2025	58081	6	Health	Pend canceled	Pend canceled	3885	3101	3263
2025	58081	6	Health	Pend canceled	Pending	1	1	1
2025	58081	6	Health	Pending	Pending	30	25	30
2025	58081	6	Health	Pending	Terminated	1	1	1
2025	58081	6	Health	Terminated	Aborted	6	4	6
2025	58081	6	Health	Terminated	Cancelled	1053	776	1019
2025	58081	6	Health	Terminated	Terminated	202166	162159	188130
2025	60224	6	Health	Aborted	Aborted	5	5	5
2025	60224	6	Health	Cancelled	Cancelled	13384	8871	11863
2025	60224	6	Health	Enrolled	Cancelled	63	47	61
2025	60224	6	Health	Enrolled	Enrolled	25660	20748	25660
2025	60224	6	Health	Enrolled	Terminated	126	115	125
2025	60224	6	Health	Pend	Pend	10	8	10
2025	60224	6	Health	Pend canceled	Pend canceled	541	390	489
2025	60224	6	Health	Pending	Pending	16	13	16
2025	60224	6	Health	Terminated	Cancelled	68	61	68
2025	60224	6	Health	Terminated	Terminated	13096	11012	12848
2025	64357	6	Dental	Cancelled	Cancelled	1035	676	914
2025	64357	6	Dental	Cancelled	Pending	2	2	2
2025	64357	6	Dental	Enrolled	Enrolled	874	604	874
2025	64357	6	Dental	Enrolled	Terminated	3	3	3
2025	64357	6	Dental	Pend canceled	Pend canceled	21	11	21
2025	64357	6	Dental	Pending	Pending	19	12	19
2025	64357	6	Dental	Terminated	Cancelled	1	1	1
2025	64357	6	Dental	Terminated	Terminated	500	354	498
2025	68806	6	Dental	Cancelled	Cancelled	9728	6132	8786
2025	68806	6	Dental	Cancelled	Pending	11	7	11
2025	68806	6	Dental	Enrolled	Cancelled	52	42	52
2025	68806	6	Dental	Enrolled	Enrolled	9529	6498	9529
2025	68806	6	Dental	Enrolled	Terminated	136	110	136
2025	68806	6	Dental	Pend	Pend	5	3	5
2025	68806	6	Dental	Pend canceled	Enrolled	1	1	1
2025	68806	6	Dental	Pend canceled	Pend canceled	339	183	318
2025	68806	6	Dental	Pend canceled	Pending	2	1	2
2025	68806	6	Dental	Pending	Pending	172	108	172
2025	68806	6	Dental	Pending	Terminated	1	1	1
2025	68806	6	Dental	Terminated	Cancelled	88	50	73
2025	68806	6	Dental	Terminated	Terminated	5044	3273	5002
2025	70893	6	Health	Aborted	Aborted	265	194	246
2025	70893	6	Health	Cancelled	Aborted	3	2	3
2025	70893	6	Health	Cancelled	Cancelled	274407	191516	222020
2025	70893	6	Health	Cancelled	Pend canceled	1	1	1
2025	70893	6	Health	Enrolled	Aborted	7	7	7
2025	70893	6	Health	Enrolled	Cancelled	2153	1682	2102
2025	70893	6	Health	Enrolled	Enrolled	661383	525519	661377
2025	70893	6	Health	Enrolled	Pending	17	12	17
2025	70893	6	Health	Enrolled	Terminated	6163	4890	6037
2025	70893	6	Health	Pend	Pend	130	107	130
2025	70893	6	Health	Pend canceled	Enrolled	142	114	138
2025	70893	6	Health	Pend canceled	Pend canceled	9372	7286	8061
2025	70893	6	Health	Pend canceled	Pending	8	7	8
2025	70893	6	Health	Pending	Cancelled	6	5	6
2025	70893	6	Health	Pending	Pending	245	161	245
2025	70893	6	Health	Pending	Terminated	5	1	5
2025	70893	6	Health	Terminated	Aborted	11	7	10
2025	70893	6	Health	Terminated	Cancelled	1872	1387	1794
2025	70893	6	Health	Terminated	Terminated	271072	207289	232695
2025	82824	6	Health	Aborted	Aborted	19	13	18
2025	82824	6	Health	Cancelled	Cancelled	66748	46219	57636
2025	82824	6	Health	Enrolled	Cancelled	161	131	158
2025	82824	6	Health	Enrolled	Enrolled	58724	44702	58724
2025	82824	6	Health	Enrolled	Terminated	437	370	436
2025	82824	6	Health	Pend	Pend	27	14	27
2025	82824	6	Health	Pend canceled	Pend canceled	1248	837	1063
2025	82824	6	Health	Pend canceled	Pending	1	1	1
2025	82824	6	Health	Pending	Pending	4	3	4
2025	82824	6	Health	Terminated	Cancelled	271	208	269
2025	82824	6	Health	Terminated	Terminated	61968	50827	60427
2025	83502	6	Dental	Cancelled	Cancelled	1274	935	1195
2025	83502	6	Dental	Enrolled	Cancelled	2	2	2
2025	83502	6	Dental	Enrolled	Enrolled	1185	868	1185
2025	83502	6	Dental	Enrolled	Terminated	6	6	6
2025	83502	6	Dental	Pend canceled	Pend canceled	33	23	32
2025	83502	6	Dental	Terminated	Cancelled	13	7	10
2025	83502	6	Dental	Terminated	Terminated	792	601	784
2025	83761	6	Health	Aborted	Aborted	12	8	12
2025	83761	6	Health	Cancelled	Cancelled	30449	18703	25518
2025	83761	6	Health	Enrolled	Cancelled	269	222	264
2025	83761	6	Health	Enrolled	Enrolled	55229	38043	55229
2025	83761	6	Health	Enrolled	Terminated	572	494	559
2025	83761	6	Health	Pend	Pend	16	12	16
2025	83761	6	Health	Pend canceled	Pend canceled	1395	898	1227
2025	83761	6	Health	Pending	Pending	43	29	43
2025	83761	6	Health	Terminated	Cancelled	180	138	178
2025	83761	6	Health	Terminated	Terminated	20119	14522	18965
2025	86637	6	Dental	Aborted	Aborted	1	1	1
2025	86637	6	Dental	Cancelled	Cancelled	6536	4170	6070
2025	86637	6	Dental	Cancelled	Pending	5	4	5
2025	86637	6	Dental	Enrolled	Cancelled	38	34	38
2025	86637	6	Dental	Enrolled	Enrolled	9005	5989	9005
2025	86637	6	Dental	Enrolled	Terminated	76	62	76
2025	86637	6	Dental	Pend	Pend	5	3	5
2025	86637	6	Dental	Pend canceled	Enrolled	4	1	4
2025	86637	6	Dental	Pend canceled	Pend canceled	296	195	280
2025	86637	6	Dental	Pending	Pending	64	43	64
2025	86637	6	Dental	Terminated	Cancelled	40	32	38
2025	86637	6	Dental	Terminated	Terminated	5580	3829	5503
2025	89942	6	Health	Aborted	Aborted	7	4	7
2025	89942	6	Health	Cancelled	Cancelled	41862	26945	33884
2025	89942	6	Health	Cancelled	Pend canceled	3	1	3
2025	89942	6	Health	Enrolled	Aborted	1	1	1
2025	89942	6	Health	Enrolled	Cancelled	315	262	312
2025	89942	6	Health	Enrolled	Enrolled	69334	47742	69334
2025	89942	6	Health	Enrolled	Terminated	719	582	707
2025	89942	6	Health	Pend	Pend	26	23	26
2025	89942	6	Health	Pend canceled	Enrolled	9	9	8
2025	89942	6	Health	Pend canceled	Pend canceled	1511	1090	1315
2025	89942	6	Health	Pend canceled	Pending	2	2	2
2025	89942	6	Health	Pending	Pending	73	51	73
2025	89942	6	Health	Terminated	Aborted	2	2	2
2025	89942	6	Health	Terminated	Cancelled	263	191	245
2025	89942	6	Health	Terminated	Terminated	27559	19844	25187

================================================================

SELECT
    coverage_year,
    hios_issuer_id,
    MONTH(GAA_Load_Datetime) AS load_month,
    COUNT(*) AS row_count,
    COUNT(DISTINCT enrollment_id) AS enrollment_count,
    COUNT(DISTINCT enrollee_id) AS enrollee_count
FROM dbo.Enrollments_TEST
WHERE coverage_year = 2025
GROUP BY
    coverage_year,
    hios_issuer_id,
    MONTH(GAA_Load_Datetime)
ORDER BY
    hios_issuer_id,
    load_month;
2025	13535	6	2651	1856	2551
2025	15105	6	56821	42478	47249
2025	37001	6	12396	9263	10956
2025	37301	6	11733	7853	10413
2025	43802	6	33398	22668	30209
2025	45334	6	161927	132861	137206
2025	49046	6	199675	136597	156241
2025	58081	6	631413	457354	476571
2025	60224	6	52969	41047	47357
2025	64357	6	2455	1657	2230
2025	68806	6	25108	16198	22399
2025	70893	6	1227262	932187	914980
2025	82824	6	189608	142615	158404
2025	83502	6	3305	2427	2998
2025	83761	6	108284	72215	83485
2025	86637	6	21650	14231	19439
2025	89942	6	141686	95709	107560
